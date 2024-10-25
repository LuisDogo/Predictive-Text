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
    ldms = pd.read_csv("corpora/LDMS.csv")
    rrm = pd.read_csv("corpora/RubenChatsJoined.csv").dropna(subset=["content"])
    eyag = pd.read_csv("corpora/EYAG.csv").dropna(subset=["content"])
    # dahb = pd.read_csv()
    corpora = {
        "Moreno_Santamaria_Luis_Daniel" : ldms["content"],
        "Ruben_Rodriguez_Mendez" : rrm["content"],
        "Edwin_Yahir_Arteaga_Gonzalez" : eyag["content"],
        "Diego_Alberto_Hernandez_Barrera" : 0
    }
    for alumno in corpora:
        # .csv creation
        for ngram in range(2,n):
            ngrams_file_name = f'ngrams/ngrams_{ngram}_{alumno}'
            vectorizer = CountVectorizer(ngram_range = (ngram, ngram))
            ft_matrix = vectorizer.fit_transform(corpora[alumno])
            df_ngram = pd.DataFrame(ft_matrix) 
            df_ngram.to_csv(ngrams_file_name, sep = "\t")
    return 0


if __name__ == "__main__":
    main()