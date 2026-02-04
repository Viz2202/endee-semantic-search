from embed import embed_texts
from index import create_index

def ingest_documents(documents):
    index = create_index()

    embeddings = embed_texts(documents)

    payload = [
        {
            "id": f"doc{i}",
            "vector": embeddings[i],
            "metadata": {
                "text": documents[i],
                "category": "tech"
            }
        }
        for i in range(len(documents))
    ]

    index.upsert(payload)
    print("Documents successfully ingested into Endee.")
