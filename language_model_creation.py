from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
import pickle



def main():
    pipe = Pipeline([("normalization", ), ("tokenization", )]) # (key, estimator)
    return 0


if __name__ == "__main__":
    main()