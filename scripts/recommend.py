import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load assessment catalog
catalog = pd.read_csv("shl_catalog.csv")

# 2. Fill empty descriptions
catalog["description"] = catalog["description"].fillna("")

# 3. Convert descriptions into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
assessment_vectors = vectorizer.fit_transform(catalog["description"])

def recommend_assessments(query, top_k=5):
    # 4. Convert query into vector
    query_vector = vectorizer.transform([query])

    # 5. Compute similarity
    similarities = cosine_similarity(query_vector, assessment_vectors)[0]

    # 6. Get top matches
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = catalog.iloc[top_indices][["name", "url"]]
    return results

# 7. Test it
if __name__ == "__main__":
    test_query = "Looking for a Java developer with good communication skills"
    results = recommend_assessments(test_query, top_k=5)
    print(results)

