import re
from collections import Counter

def count_words(text):
    # Remove punctuation and convert text to lowercas
    text = #ToDo
    
    # Split the text into words
    words =#ToDo
    
    # Count the frequency of each word using Counter
    word_counts = Counter(words)
    
    return word_counts

# Example usage:
if __name__ == "__main__":
    input_text = """
    This is a sample text. This text contains some words, and some words are repeated.
    The program should count how many times each word appears in this text.
    """
    
    word_counts = count_words(input_text)
    
    # Print the word counts
    for word, count in #ToDo :
        print(f"'{word}': {count}")