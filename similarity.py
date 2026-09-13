import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(items):
    ids = [item.id for item in items]
    features_list = [item.features for item in items]

    df = pd.DataFrame(features_list).fillna(0) # if an item doesn't have a feature fill with 0
    similarity_matrix = cosine_similarity(df)

    return ids, similarity_matrix
