from sklearn.feature_extraction.text import CountVectorizer
import spacy
import numpy as np
import pandas as pd
import pickle
import os.path
import sys

def sentence():
    return 0

def main():
    # hyperparameters

    nlp = spacy.load("es_core_news_sm")
    n = 4

    # corpora creation

    df = pd.read_csv("corpora/LDMS.csv")
    corpora = {
        "Moreno_Santamaria_Luis_Daniel" : df["content"]
    }

    for alumno in corpora:
        ngrams_file_name = f'ngrams/ngrams_{alumno}'
        # .csv creation
        for ngram in range(2,n):
            vectorizer = CountVectorizer(ngram_range = (ngram, ngram))
            ft_matrix = vectorizer.fit_transform(corpora[alumno])
            print(ft_matrix)
            print("==" * 50)

    return 0


if __name__ == "__main__":
    main()