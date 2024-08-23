def all_variants(text):
    for i in range(len(text)):
        yield text[i]

    for i in range(len(text) - 1):
        yield text[i:i + 2]

    yield text


a = all_variants("abc")
for i in a:
    print(i)
