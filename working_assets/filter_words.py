def load_words():
    with open('words.txt') as word_file:
        valid_words = word_file.read().split()

    return valid_words


if __name__ == '__main__':
    words = load_words()
    six_letter_words = [x for x in words if len(x) == 6]
    print(six_letter_words)
    