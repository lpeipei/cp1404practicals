def main():
    text = input("Enter your text: ")
    word_count = count_word_occurrences(text)
    max_word_length = max(len(word) for word in word_count.keys())

    for word, count in sorted(word_count.items()):
        print(f"{word:{max_word_length}} : {count}")


def count_word_occurrences(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


main()
