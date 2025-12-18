import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load catalog
catalog = pd.read_csv("../data/shl_catalog.csv")
catalog["description"] = catalog["description"].fillna("")

# Build TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
assessment_vectors = vectorizer.fit_transform(catalog["description"])

def recommend_urls(query, top_k=10):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, assessment_vectors)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    return catalog.iloc[top_indices]["url"].tolist()

# Load provided dataset
df = df = pd.read_excel("../data/Gen_AI Dataset.xlsx")

rows = []

# Generate predictions
for query in df["Query"].unique():
    urls = recommend_urls(query, top_k=10)
    for url in urls:
        rows.append({
            "Query": query,
            "Assessment_url": url
        })

# Save submission CSV
submission = pd.DataFrame(rows)
submission.to_csv("submission.csv", index=False)

print("DONE ✅ submission.csv created with", len(submission), "rows")
