# -*- coding: utf-8 -*-
"""Copy of natural_language_processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dK2Qt7lm7i7bFqSHaC8cPCZkpPch3QWT

# Natural Language Processing

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

"""## Cleaning the texts"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
  review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) #changing every character into space except letters
  review = review.lower()    # Turning into Lower cases
  review = review.split()    # Splitting into words to apply stemming
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')   # getting all the stops words (#@, in, and, the, etc)
  all_stopwords.remove('not')         # getting all the stopwords excluding 'not'
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]   # applying stemming (not on stopwords)
  review = ' '.join(review)   # rejoining all the words into String (e.g sentences again)
  corpus.append(review)       # Appending into list

print(corpus)

"""## Creating the Bag of Words model"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)  # total columns generated without using parameter, are 1566 but using manually 1500 to remove some words whcih are still present and not useful i.e steve, pho etc
X = cv.fit_transform(corpus).toarray()     # fit takes all the words from reviews and 'transform' put them into columns
y = dataset.iloc[:, -1].values             # we have used .toarray in previous line of code as matrix of features should be 2d array
                                           # so  can be used for splitting of Training and Test set

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

"""## Training the Naive Bayes model on the Training set"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

"""## Predicting the Test set results"""

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)