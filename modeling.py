#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:38:23 2022

@author: chenzhiyi
"""

# %%%%%%%
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from textblob import TextBlob

from wordcloud import WordCloud

def word(data,bgcolor,title):
    plt.figure(figsize = (50,50))
    word = WordCloud(background_color = bgcolor, max_words = 2000, random_state=42, max_font_size = 50)
    word.generate(' '.join(data))
    plt.imshow(word)
    plt.axis('off')

# %%%%%%%

dta = pd.read_csv("/Users/chenzhiyi/Documents/BUS 256A/interview_review.csv")

dta.head()

# %%%%%%%

polarity = []
subjectivity = []

for i in dta['interview'].values:
    try:
        analysis =TextBlob(i)
        polarity.append(analysis.sentiment.polarity)
        subjectivity.append(analysis.sentiment.subjectivity)
        
    except:
        polarity.append(0)
        subjectivity.append(0)

dta['polarity'] = polarity
dta['subjectivity'] = subjectivity
#positive polarity
word(dta['interview'][dta.polarity>0],'black','Common Words' )
#negative polarity
word(dta['interview'][dta.polarity<0],'black','Common Words' )

dta['polarity'][dta.polarity==0]= 0
dta['polarity'][dta.polarity > 0]= 1
dta['polarity'][dta.polarity < 0]= -1
dta.polarity.value_counts().plot.bar()

# %%%%%%%

# sentiment

dta['experience'][dta.experience == 'Positive Experience'] = 0
dta['experience'][dta.experience == 'Negative Experience'] = 1
dta['experience'][dta.experience == 'Neutral Experience'] = 2

dt1 = dta[['experience', 'interview']]
dt1 = dt1.drop(labels=[85, 232, 247, 253, 242, 244], axis=0)
dt1['experience']= dt1['experience'].fillna(dt1['experience'].median())

vectorizer = CountVectorizer(lowercase=True, min_df = 0.0, max_df = 1.0, ngram_range = (1,1))
X = vectorizer.fit_transform(dt1.interview)
count_X = X.toarray()

X_train, X_test, y_train, y_test = train_test_split(count_X, dt1['experience'], test_size=0.2)

# logistic regression

log = LogisticRegression()
log.fit(X_train, y_train)
print(log.score(X_train, y_train))
print(log.score(X_test, y_test))
pred = log.predict(X_test)
cm = confusion_matrix(y_test, pred)

# random forest
forest = RandomForestClassifier()
forest.fit(X_train, y_train)
print(forest.score(X_train, y_train))
print(forest.score(X_test, y_test))
pred = forest.predict(X_test)
accuracy = accuracy_score(y_test, pred)
print(accuracy)


