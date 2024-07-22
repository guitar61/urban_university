import hashlib
from typing import List
from time import sleep


class User:
    def __init__(self, username: str, password: str, age: int):
        self.nickname = username
        self.password = self._hash_password(password)
        self.age = age

    def _hash_password(self, password: str) -> int:
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def check_password(self, password: str) -> bool:
        return self.password == self._hash_password(password)

    def __repr__(self):
        return f"{self.nickname}"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and self.password == other.password
        return False

    def __contains__(self, nickname):
        return self.nickname == nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, time_now={self.time_now}, adult_mode={self.adult_mode})"

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False

    def __contains__(self, title):
        return self.title == title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                return f"User {nickname} logged in successfully."
        return "Invalid nickname or password."

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                return f"User {nickname} already exists."

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        return f"User {nickname} registered and logged in successfully."

    def log_out(self):
        self.current_user = None
        return "User logged out successfully."

    def add(self, *videos: Video):
        existing_titles = {video.title for video in self.videos}
        for video in videos:
            if video.title not in existing_titles:
                self.videos.append(video)

    def get_videos(self, search_term: str) -> List[str]:
        search_term_lower = search_term.lower()
        return [video.title for video in self.videos if search_term_lower in video.title.lower()]

    def watch_video(self, title: str):
        if not self.current_user:
            print("Log in to watch the video")
            return "Log in to watch the video"

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("You are under 18, please leave the page")
                    return "You are under 18, please leave the page"

                print(f"Watching '{title}' at second {video.time_now}.")
                while video.time_now < video.duration:
                    sleep(1)
                    video.time_now += 1
                    print(f"{video.time_now}", end=" ", flush=True)
                video.time_now = 0
                print("End of video")
                return "End of video"

        print("Video not found.")
        return "Video not found."

    def __repr__(self):
        return f"UrTube(current_user={self.current_user})"


# Verification code
ur = UrTube()
v1 = Video('The Best Programming Language of 2024', 200)
v2 = Video('Why Do Girls Want a Guy Programmer?', 10, adult_mode=True)

# Adding Videos
ur.add(v1, v2)

# Checking Search
print(ur.get_videos('Best'))
print(ur.get_videos('PROG'))

# Checking User Login and Age Limit
ur.watch_video('Why Do Girls Want a Guy Programmer?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Why Do Girls Want a Guy Programmer?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Why Do Girls Want a Guy Programmer?')

# Checking Login another account
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Trying to play a non-existent video
ur.watch_video('The best programming language of 2024!')
