import os
import openai
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize OpenAI client using base_url and API key
client = openai.OpenAI(
    base_url="https://aiportalapi.stu-platform.live/jpe",
    api_key="YOUR_API_KEY_HERE"  # Replace with your actual API key
)

# Function to check if a vector is valid (not None, no NaN or Inf values)
def is_valid_vector(vec):
    return vec is not None and not np.isnan(vec).any() and not np.isinf(vec).any()

# Function to normalize a vector
def normalize(v):
    norm = np.linalg.norm(v)
    return v / norm if norm > 0 else v

# Sample dataset: clothing products with names and descriptions
products = [
    {"name": "Blue Linen Shirt", "description": "A lightweight blue shirt perfect for summer."},
    {"name": "Black Leather Jacket", "description": "A stylish and durable black leather jacket."},
    {"name": "Cotton T-Shirt", "description": "Simple white t-shirt made from 100% cotton."},
    {"name": "Running Shoes", "description": "Lightweight shoes designed for long-distance running."},
    {"name": "Wool Winter Coat", "description": "Thick and warm coat for cold winter weather."},
    {"name": "Floral Summer Dress", "description": "Colorful dress ideal for summer outings."},
    {"name": "Slim Fit Jeans", "description": "Classic blue jeans with a modern slim fit."},
    {"name": "Rain Jacket", "description": "Water-resistant jacket with hood, perfect for rainy days."},
    {"name": "Sports Shorts", "description": "Breathable shorts suitable for workouts and running."},
    {"name": "Silk Blouse", "description": "Elegant silk blouse, comfortable and classy."}
]

# Function to get text embedding from OpenAI API
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Precompute and normalize product embeddings
product_embeddings = []
valid_indices = []
for idx, item in enumerate(products):
    combined_text = f"{item['name']} {item['description']}"
    embedding = get_embedding(combined_text)
    if is_valid_vector(embedding):
        product_embeddings.append(normalize(embedding))
        valid_indices.append(idx)
    else:
        print(f"Invalid embedding skipped for: {item['name']}")

# Search function: computes similarity between user query and product embeddings
def search_products(query, top_k=3):
    raw_embedding = get_embedding(query)
    if not is_valid_vector(raw_embedding):
        print("Query embedding is invalid.")
        return

    query_embedding = normalize(raw_embedding)
    if not is_valid_vector(query_embedding):
        print("Normalized query embedding is invalid.")
        return

    # Recheck all product embeddings before similarity
    valid_product_embeddings = []
    valid_indices_checked = []
    for i, emb in enumerate(product_embeddings):
        if is_valid_vector(emb):
            valid_product_embeddings.append(emb)
            valid_indices_checked.append(valid_indices[i])

    if not valid_product_embeddings:
        print("No valid product embeddings to compare.")
        return

    similarities = cosine_similarity([query_embedding], valid_product_embeddings)[0]

    # Rank and print
    ranked_results = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)[:top_k]
    print(f"\nQuery:  {query} \nTop {top_k} matching products:")
    for idx, score in ranked_results:
        product = products[valid_indices_checked[idx]]
        print(f"- {product['name']} ({score:.3f})\n  {product['description']}\n")

# Main entry point
if __name__ == "__main__":
    user_query = input("Enter your search query: ")
    search_products(user_query)