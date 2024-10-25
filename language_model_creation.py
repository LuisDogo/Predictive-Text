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

    # corpora creation

    df = pd.read_csv("corpora/LDMS.csv")
    corpora = {
        "Moreno_Santamaria_Luis_Daniel" : df["content"]
    }
    # aftermath

    corpora_tokens = []
    for alumno in corpora:
        corpus_alumno = corpora[alumno].apply(nlp)
        tokens_file_name = f'tokens/tokens_{alumno}'
        if(os.path.exists(tokens_file_name)):
            return 0
        else:
            tokens_file = open(tokens_file_name, "wb")
            pickle.dump(corpus_alumno, tokens_file)
            tokens_file.close()

    return 0


if __name__ == "__main__":
    main()

# if(os.path.exists(vsm_file_name)):
#     print('Ya existe')
#     vsm_file = open(vsm_file_name,'rb')
#     vsm = pickle.load(vsm_file)
# else:
#     norm_df = df_norm(contenido, 6)
#     vsm = vector_space_model(norm_df, contexto, unit_vector)
#     vsm_file = open(vsm_file_name,'wb')
#     pickle.dump(vsm, vsm_file)
#     vsm_file.close()
#     ft_vsm_file = open(ft_vsm_file_name,'wb')
#     pickle.dump(vsm.ft_matrix, ft_vsm_file)
#     ft_vsm_file.close()