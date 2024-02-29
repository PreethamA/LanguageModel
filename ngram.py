from collections import Counter
import re

def find_ngrams(text, n):
    """
    Function to find n-grams in a given text.

    Args:
    text (str): The input text.
    n (int): The size of the n-grams.

    Returns:
    list: List of n-grams found in the text.
    """
    # Tokenize the text
    words = re.findall(r'\w+', text.lower())

    # Generate n-grams
    ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]

    return ngrams

def main():
    file_path = input("Enter the path to the text file: ")
    n = int(input("Enter the size of n for n-grams: "))

    try:
        with open(file_path, 'r') as file:
            text = file.read()
            ngrams = find_ngrams(text, n)
            ngram_counts = Counter(ngrams)

            print(f"Top {n}-grams:")
            for ngram, count in ngram_counts.most_common(10):
                print(' '.join(ngram), "-", count)

    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    main()

