class WordsFinder:
    def __init__(self, *file_names):
        # Store the file names in a list
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        # List of punctuation to remove
        punctuation = [',', '.', '=', '!', '?', ';', ':']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        # Convert the line to lowercase
                        line = line.lower()
                        # Remove punctuation
                        for punct in punctuation:
                            line = line.replace(punct, '')
                        # Split the line into words
                        words.extend(line.split())
                    # Store the list of words in the dictionary
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File {file_name} not found.")
                all_words[file_name] = []
            except Exception as e:
                print(f"An error occurred while reading {file_name}: {e}")
                all_words[file_name] = []

        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            try:
                # Find the first occurrence of the word
                position = words.index(word) + 1  # Convert to 1-based index
            except ValueError:
                # If the word is not found, set position to -1
                position = -1

            word_positions[file_name] = position

        return word_positions

    def count(self, word):
        word = word.lower()
        word_counts = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            # Count the occurrences of the word
            count = words.count(word)
            word_counts[file_name] = count

        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
