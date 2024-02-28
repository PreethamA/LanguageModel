import math

def calculate_perplexity(text, ngram_order):
    words = text.split()
    total_words = len(words)
    ngrams = [tuple(words[i:i+ngram_order]) for i in range(total_words - ngram_order + 1)]
    
    # Count occurrences of each n-gram
    ngram_counts = {}
    for ngram in ngrams:
        ngram_counts[ngram] = ngram_counts.get(ngram, 0) + 1
    
    # Calculate perplexity
    perplexity = 1.0
    for ngram in ngrams:
        probability = ngram_counts.get(ngram, 0) / float(total_words - ngram_order + 1)
        perplexity *= (1/probability)
    
    perplexity = pow(perplexity, 1/total_words)
    return perplexity

def main():
    file_path = input("Enter the path to the text file: ")
    ngram_order = int(input("Enter the n-gram order: "))
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        perplexity = calculate_perplexity(text, ngram_order)
        print("Perplexity:", perplexity)
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()


