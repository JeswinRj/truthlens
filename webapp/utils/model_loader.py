import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

def load_pickle(filename):
    with open(os.path.join(MODEL_DIR, filename), "rb") as f:
        return pickle.load(f)

LR = load_pickle("logistic_regression.pkl")
DT = load_pickle("decision_tree.pkl")
GB = load_pickle("gradient_boosting.pkl")
RF = load_pickle("random_forest.pkl")
VECTORIZER = load_pickle("tfidf_vectorizer.pkl")
