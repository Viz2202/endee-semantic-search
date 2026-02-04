# Endee Semantic Search 🚀

## Project Description

This project demonstrates a semantic search system built using **Endee (nD)** as a high-performance vector database. Text documents are converted into embeddings using a transformer-based model, stored in Endee, and queried using vector similarity to retrieve semantically relevant results.

The project focuses on system design and integration, showcasing how a modern AI workflow combines:
- Pretrained embedding models
- A vector database
- Docker-based deployment

---

## Problem Statement

Traditional keyword-based search fails to capture semantic meaning. For example, a query like **"What is deep learning?"** may not match documents that do not contain those exact words.

**Semantic search** solves this by:
- Converting text into numerical vectors (embeddings)
- Retrieving documents based on **meaning**, not keywords

---

## Solution Overview

This project implements a semantic search pipeline where:

1. Text documents are embedded using a transformer model
2. Embeddings are stored in Endee
3. User queries are embedded and searched using cosine similarity
4. The most semantically similar documents are returned

---

## System Architecture

```
User Query
    ↓
SentenceTransformer (Python)
    ↓
Dimensional Embeddings
    ↓
Endee Vector Database (Docker)
    ↓
Top-K Similar Documents
```

---

## How Endee Is Used

**Endee** acts as the core vector database in this system.

Endee is responsible for:
- Storing high-dimensional embeddings
- Indexing vectors using cosine similarity
- Performing fast similarity search using INT8 quantization

The system fails when Endee is stopped, proving that **Endee is essential** for storage and retrieval.

---

## Project Structure

```
endee-semantic-search/
│
├── src/
│   ├── embed.py       # Embedding generation
│   ├── index.py       # Endee index configuration
│   ├── ingest.py      # Vector insertion into Endee
│   └── search.py      # Semantic search logic
│
├── endee/
│   └── docker-compose.yml # Endee service configuration
│
├── notebooks/
│   └── semantic_search_experiment.ipynb     # End-to-end demonstration
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

- **Endee (nD)** – Vector database
- **SentenceTransformers** – Text embedding model
- **Docker & Docker Compose** – Deployment
- **Python** – Client logic
- **Jupyter Notebook** – Demonstration

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Viz2202/endee-semantic-search.git
cd endee-semantic-search
```

### 2. Start Endee using Docker

```bash
cd endee-semantic-search/endee
docker compose up
```

Verify Endee is running by opening: [http://localhost:8080](http://localhost:8080)

### 3. Set up Python environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the demo

```bash
jupyter notebook
```

Open: `notebooks/semantic_search_experiment.ipynb`

Run all cells to ingest documents and perform semantic search.

## Key Design Decisions

- **dimensional embeddings** – Matches the output of the embedding model
- **Cosine similarity** – Best suited for text embeddings
- **INT8 quantization** – Improves performance and memory efficiency
- **Model–database decoupling** – Endee stores vectors only; the embedding model runs separately in Python

---

## Notes

- A small dataset is used for demonstration purposes
- The system can be extended to larger datasets or RAG pipelines
- Endee is deployed using Docker for reproducibility

---

## Conclusion

This project demonstrates a complete, minimal, and production-style semantic search system using **Endee** as a vector database. It highlights modern AI system design principles where pretrained models, vector databases, and containerized services work together.

---

