result1 = ('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = ('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')


def single_root_words(root_word, *other_words):
same_words = []
root_word_lower = root_word.lower()

for word in other_words:
if word.lower() in root_word_lower or root_word_lower in word.lower():
same_words.append(word)

return same_words


# unpacking the tuple as arguments inside the function.
print(single_root_words(*result1))
print(single_root_words(*result2))
