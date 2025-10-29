
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import joblib
import re

DATA_PATH = "netflix_titles.csv"
ARTIFACT_DIR = "artifacts"

os.makedirs(ARTIFACT_DIR, exist_ok=True)

def clean_text(s):
    if pd.isna(s):
        return ""
    s = str(s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s,]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def build_corpus(df):
    fields = ['title', 'listed_in', 'description', 'director', 'cast', 'country']
    for f in fields:
        if f not in df.columns:
            df[f] = ""
    corpus = (df['title'].fillna('') + " " +
              df['listed_in'].fillna('') + " " +
              df['description'].fillna('') + " " +
              df['director'].fillna('') + " " +
              df['cast'].fillna('') + " " +
              df['country'].fillna(''))
    corpus = corpus.apply(clean_text)
    return corpus

def main():
    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    df = df.drop_duplicates(subset=['title']).reset_index(drop=True)

    corpus = build_corpus(df)
    print("Corpus built.")

    tfidf = TfidfVectorizer(max_df=0.8, min_df=1, ngram_range=(1,2), stop_words='english')
    tfidf_matrix = tfidf.fit_transform(corpus)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    joblib.dump(df, os.path.join(ARTIFACT_DIR, "metadata_df.joblib"))
    joblib.dump(tfidf, os.path.join(ARTIFACT_DIR, "tfidf.joblib"))
    joblib.dump(cosine_sim, os.path.join(ARTIFACT_DIR, "cosine_sim.joblib"))

    print("✅ Artifacts saved in:", ARTIFACT_DIR)

if __name__ == "__main__":
    main()
