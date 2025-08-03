# Assignment 08 – Semantic Search for Clothing Products

This project demonstrates how to build a semantic search engine for clothing products using OpenAI text embeddings and cosine similarity.

---

## ✅ Features

- Converts product descriptions and user queries into semantic vector embeddings
- Computes cosine similarity to find the most relevant clothing items
- Returns top matching products based on meaning, not just keywords

---

## 🧠 Technologies Used

- OpenAI Embedding API (`text-embedding-3-small`)
- `scikit-learn` for cosine similarity calculation
- Python for scripting and logic

---

## 📥 Sample Product Dataset

The script includes 10 sample clothing products with name and description, such as:

- "Blue Linen Shirt"
- "Wool Winter Coat"
- "Slim Fit Jeans"

Each product is embedded using OpenAI's embedding model to enable semantic matching.

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install openai scikit-learn numpy
```

### 2. Set your API key

```bash
export OPENAI_API_KEY="your-api-key-here"
```

> Replace `"your-api-key-here"` with your actual OpenAI API key.

### 3. Run the script

```bash
python assignment_08_semantic_search.py
```

Then enter a search query when prompted. Example:

```
something to wear when it rains
```

---

## 📌 Notes

- Embeddings are computed using OpenAI's `text-embedding-3-small` model.
- All product embeddings are recomputed on script run (consider caching for performance).
- Ideal for building prototypes of intelligent product search or recommendation tools.

---

Happy exploring! 🧥👗👕