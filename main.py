def find_most_common_word(text):
    text = text.lower()

    for char in ".,!?:;-":
        text = text.replace(char, " ")

    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    word_keys = list(word_count.keys())
    word_keys.sort()
    word_keys = word_keys
    word_dict_sorted = {i: word_count[i] for i in word_keys}

    less_common_word = None
    for word in word_dict_sorted:
        if (
            less_common_word is None
            or word_dict_sorted[word] < word_dict_sorted[less_common_word]
        ):
            less_common_word = word

    print(less_common_word)


find_most_common_word(
    "I bought two books: a new book and an old book. The new book was more expensive than the old book."
)
