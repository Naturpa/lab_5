import sys
from collections import defaultdict

def process_text():
    word_positions = defaultdict(list)
    word_list = []

    for line in sys.stdin:
        words = line.split()
        for index, word in enumerate(words):
            if word.istitle():
                if word not in word_positions:
                    word_positions[word].append(index)
                word_list.append(word)

    sorted_words = sorted(set(word_list))
    result = [(word_positions[word][0], word) for word in sorted_words]

    for position, word in result:
        print(position, word)

if __name__ == "__main__":
    process_text()
