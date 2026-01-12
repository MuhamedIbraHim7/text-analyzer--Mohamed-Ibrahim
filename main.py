"""
Text Analyzer - Analyzes text and returns statistics

"""

import re
from collections import Counter
from typing import Dict, List, Tuple


def analyze_text(text: str) -> Dict:
    """
    Analyzes a text string and returns comprehensive statistics.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        Dict: Dictionary containing:
            - word_count: Total number of words
            - sentence_count: Total number of sentences
            - top_10_words: List of tuples [(word, frequency), ...]
    """
    
    # ========================================
    # STEP 1: WORD COUNT
    # ========================================
    # Concept: Extract all words using regex
    # Pattern \w+ matches: letters, digits, underscores
    
    words = re.findall(r'\w+', text)
    word_count = len(words)
    
    
    # ========================================
    # STEP 2: SENTENCE COUNT
    # ========================================
    # Concept: Split by sentence-ending punctuation (. ! ?)
    # Pattern [.!?]+ handles multiple punctuation: "!!!" or "...?"
    
    # Split text into potential sentences
    sentences = re.split(r'[.!?]+', text)
    
    # Filter out empty strings and whitespace-only strings
    # This prevents counting trailing punctuation as extra sentences
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)
    
    
    # ========================================
    # STEP 3: TOP 10 MOST FREQUENT WORDS
    # ========================================
    # Concept: Normalize, count, and rank words
    
    # Step 3a: Normalize words (convert to lowercase)
    normalized_words = [word.lower() for word in words]
    
    # Step 3b: Count word frequencies
    # Counter is a specialized dictionary for counting
    word_freq = Counter(normalized_words)
    
    # Step 3c: Get top 10 most common words
    # Returns list of tuples: [('word', count), ...]
    top_10_words = word_freq.most_common(10)
    
    
    # ========================================
    # RETURN RESULTS
    # ========================================
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'top_10_words': top_10_words
    }


def print_analysis(results: Dict) -> None:
    """
    Pretty-prints the analysis results.
    
    Args:
        results (Dict): Results from analyze_text()
    """
    print("=" * 50)
    print("TEXT ANALYSIS RESULTS")
    print("=" * 50)
    
    print(f"\n Total Words: {results['word_count']}")
    print(f"Total Sentences: {results['sentence_count']}")
    
    print("\n Top 10 Most Frequent Words:")
    print("-" * 50)
    for rank, (word, count) in enumerate(results['top_10_words'], 1):
        print(f"{rank:2}. {word:20} → {count:3} times")
    
    print("=" * 50)


def main():
    """
    Main function: Reads sample_text.txt and analyzes it.
    """
    try:
        # Read the input file
        with open('sample_text.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Analyze the text
        results = analyze_text(text)
        
        # Display results
        print_analysis(results)
        
    except FileNotFoundError:
        print("Error: sample_text.txt not found!")
        print("Make sure the file is in the same directory as main.py")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
