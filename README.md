# 📊 Text Analyzer

A Python-based text analysis tool that provides comprehensive statistics about text documents.

## 👨‍💻 Author
**Mohamed Ibrahim** - AI Engineer @ Neqabty

## 🎯 Features

This analyzer provides:
1. **Word Count** - Total number of words in the text
2. **Sentence Count** - Number of sentences (separated by `.`, `!`, `?`)
3. **Top 10 Frequent Words** - Most commonly used words (case-insensitive)

## 🛠️ Technical Implementation

### Key Concepts Used:

- **Regular Expressions (regex)**: For robust text parsing
  - `\w+` pattern extracts words (handles contractions, hyphenated words, numbers)
  - `[.!?]+` pattern identifies sentence boundaries

- **Collections.Counter**: Efficient frequency counting
  - Automatically counts occurrences of each word
  - `.most_common(n)` method retrieves top N items

- **Text Normalization**: Converting to lowercase for accurate frequency analysis

## 📋 Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<yourname>/text-analyzer--<yourname>.git
cd text-analyzer--<yourname>
```

### 2. Install dependencies (if any)
```bash
pip install -r requirements.txt
```

### 3. Verify files
Make sure you have these files:
```
text-analyzer--<yourname>/
├── main.py
├── README.md
├── requirements.txt
└── sample_text.txt
```

## ▶️ How to Run

### Basic Usage
```bash
python main.py
```

### Expected Output
```
==================================================
📊 TEXT ANALYSIS RESULTS
==================================================

📝 Total Words: 185
📄 Total Sentences: 28

🔥 Top 10 Most Frequent Words:
--------------------------------------------------
 1. ai                  →   8 times
 2. and                 →   7 times
 3. we                  →   4 times
 4. tools               →   3 times
 5. repeat              →   3 times
 6. rag                 →   2 times
 7. 2026                →   2 times
 8. agents              →   2 times
 9. to                  →   2 times
10. prompt             →   2 times
==================================================
```

## 📊 Example with Custom Text

You can modify the code to analyze any text:

```python
from main import analyze_text

# Analyze custom text
my_text = "Hello world! This is a test. Testing is important."
results = analyze_text(my_text)

print(f"Words: {results['word_count']}")
print(f"Sentences: {results['sentence_count']}")
print(f"Top words: {results['top_10_words']}")
```

## 🧪 Testing Edge Cases

The included `sample_text.txt` tests:

- ✅ **Contractions**: don't, can't, it's
- ✅ **Hyphenated words**: end-to-end, real-world
- ✅ **MixedCase**: OpenAI, GitHub
- ✅ **Numbers**: 3.14, 1e-3
- ✅ **Symbols**: $100, 50%, #hashtags
- ✅ **URLs**: https://example.com/docs
- ✅ **Repeated patterns**: "AI AI AI"

## 🔧 Advanced Usage

### Filtering Stop Words (Optional Enhancement)

If you want to exclude common words like "the", "and", "is":

```python
# Add this to your analyze_text function
STOP_WORDS = {'the', 'and', 'is', 'a', 'to', 'of', 'in', 'it'}

# Modify step 3a:
normalized_words = [
    word.lower() for word in words 
    if word.lower() not in STOP_WORDS
]
```

### Analyzing Multiple Files

```python
import glob

for filepath in glob.glob("*.txt"):
    with open(filepath, 'r') as file:
        text = file.read()
    results = analyze_text(text)
    print(f"\nAnalysis for {filepath}:")
    print_analysis(results)
```

## 📚 Code Structure

```python
analyze_text(text: str) -> Dict
    """Main analysis function"""
    → Returns: {
        'word_count': int,
        'sentence_count': int,
        'top_10_words': List[Tuple[str, int]]
    }

print_analysis(results: Dict) -> None
    """Pretty-print results"""

main() -> None
    """Entry point: reads file and runs analysis"""
```

## 🐛 Troubleshooting

### File Not Found Error
```
❌ Error: sample_text.txt not found!
```
**Solution**: Make sure `sample_text.txt` is in the same directory as `main.py`

### Encoding Issues
If you see strange characters, ensure UTF-8 encoding:
```python
with open('sample_text.txt', 'r', encoding='utf-8') as file:
```

## 🎓 Learning Resources

### Regular Expressions
- [Python Regex Documentation](https://docs.python.org/3/library/re.html)
- [Regex101](https://regex101.com/) - Test patterns interactively

### Collections Module
- [Counter Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this repo and submit pull requests for improvements!

---

**Built with ❤️ by Mohamed Ibrahim**  
*AI Engineer | Neqabty | ENGO Misr*
