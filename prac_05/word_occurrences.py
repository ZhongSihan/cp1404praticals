def main():
    text = input("Text: ").strip()
    words = text.split()
    word_counts = {}

    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.keys())
    max_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")

main()
