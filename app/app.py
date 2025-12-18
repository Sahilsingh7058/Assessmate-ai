from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
catalog = pd.read_csv("../data/shl_catalog.csv")
catalog["description"] = catalog["description"].fillna("")

# Build TF-IDF model
vectorizer = TfidfVectorizer(stop_words="english")
assessment_vectors = vectorizer.fit_transform(catalog["description"])

# FastAPI app
app = FastAPI(title="SHL Assessment Recommendation API")

class QueryRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend(request: QueryRequest):
    query_vector = vectorizer.transform([request.query])
    similarities = cosine_similarity(query_vector, assessment_vectors)[0]

    top_indices = similarities.argsort()[-10:][::-1]
    results = catalog.iloc[top_indices]

    response = []
    for _, row in results.iterrows():
        response.append({
            "name": row["name"],
            "url": row["url"]
        })

    return {"recommended_assessments": response}
