import hashlib
from typing import List
import time

class User:
    def __init__(self, username: str, password: str, age: int):
        self.nickname = username
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password: str) -> int:
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def verify_password(self, password: str) -> bool:
        return self.password == self.hash_password(password)

class Video:
    def __init__(self, title: str, duration: int, second_to_stop: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_on = second_to_stop
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self, user_list: List[User] = None, video_list: List[Video] = None, current_user: User = None):
        self.users = user_list if user_list is not None else []
        self.videos = video_list if video_list is not None else []
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and user.verify_password(password):
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                return f"User {nickname} already exists"
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        existing_titles = {video.title for video in self.videos}
        for new_video in videos:
            if new_video.title not in existing_titles:
                self.videos.append(new_video)

    def get_videos(self, search_term: str):
        search_term_lower = search_term.lower()
        matching_titles = [video.title for video in self.videos if search_term_lower in video.title.lower()]
        return matching_titles

    def watch_video(self, video_title: str):
        # Step 1: Check if user is logged in
        if not self.current_user:
            print("Log in to your account to watch the video")
            return

        # Step 2: Find the video
        for video in self.videos:
            if video.title == video_title:
                # Step 3: Check age restriction
                if video.adult_mode and self.current_user.age < 18:
                    print("You are under 18 years old, please leave the page")
                    return

                # Step 4: Play the video
                while video.time_on < video.duration:
                    video.time_on += 1
                    print(video.time_on, end=" ", flush=True)
                    time.sleep(1)

                # Step 5: End of video
                print("End of video")
                video.time_on = 0
                return

        print("Video not found")

# Example usage
ur = UrTube()
v1 = Video('The Best Programming Language of 2024', 10)
v2 = Video('Why Do Girls Want a Programmer Boyfriend?', 10, adult_mode=True)

# Adding Videos
ur.add(v1, v2)

# Checking Search
print(ur.get_videos('Best'))  # Expect: ['The Best Programming Language of 2024']
print(ur.get_videos('PROG'))  # Expect: ['The Best Programming Language of 2024',
# 'Why Do Girls Want a Programmer Boyfriend?']

# Checking User Login and Age Limit
ur.watch_video('Why Do Girls Want a Programmer Boyfriend?')  # Expect: Log in to your account to watch the video
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Register a 13-year-old user
ur.watch_video('Why Do Girls Want a Programmer Boyfriend?')  # Expect: You are under 18 years old, please leave the page
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Register a 25-year-old user
ur.watch_video('Why Do Girls Want a Programmer Boyfriend?')  # Expect: 1 2 3 4 5 6 7 8 9 10 End of video

# Checking Login another account
print(ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55))  
# Attempt to re-register an existing user, Expect: User vasya_pupkin already exists
print(ur.current_user.nickname)  # Should output 'urban_pythonist'

# Trying to play a non-existent video
ur.watch_video('The best programming language of 2024!')  # Expect: Video not found
