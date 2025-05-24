
# Sentiment Analysis on Restaurant Reviews

This project performs Natural Language Processing (NLP) to classify restaurant reviews as positive or negative using a Naive Bayes classifier.

## 🧠 Model Overview

- **Goal**: Predict sentiment (positive/negative) of restaurant reviews.
- **Dataset**: 1,000 reviews from `Restaurant_Reviews.tsv`.

## ✨ Features

- Text cleaning and preprocessing pipeline.
- Bag of Words model with feature limitation.
- Sentiment prediction using Gaussian Naive Bayes.
- Performance evaluation using accuracy and confusion matrix.

## 🧹 Data Preprocessing

- Removed non-alphabetic characters.
- Converted to lowercase.
- Tokenized into words.
- Removed stopwords (excluding "not").
- Applied Porter Stemming.
- Reconstructed into cleaned text corpus.

## 🧰 Feature Extraction

- Used **Bag of Words** model with `CountVectorizer`.
- Limited features to top 1500 words.

## 🤖 Modeling

- **Classifier**: Gaussian Naive Bayes
- **Train/Test Split**: 80/20

## 📊 Evaluation

- Confusion Matrix and Accuracy Score used to assess performance.

## 🛠 Installation

1. Clone this repository:
```bash
git clone https://github.com/MaddyRizvi/Natural-Language-Processing_sentiment_analysis.git
cd Natural-Language-Processing_sentiment_analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Ensure you have the dataset `Restaurant_Reviews.tsv` in the project directory.
2. Run the script:
```bash
python natural_language_processing.py
```

## 📁 Files

- `Restaurant_Reviews.tsv`: Dataset file.
- `natural_language_processing.py`: Main script for training and testing.
- `README.md`: Project overview and instructions (this file).
- `CONTRIBUTING.md`: Guidelines for contributing.

## ✅ Requirements

- numpy
- pandas
- matplotlib
- scikit-learn
- nltk

## 🙌 Contributing

We welcome contributions! Please read the [CONTRIBUTING.md](./CONTRIBUTING.md) file for guidelines.

---
