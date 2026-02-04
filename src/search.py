from embed import embed_text
from index import create_index

def semantic_search(query, top_k=3):
    index = create_index()

    query_vector = embed_text([query])[0]
    results = index.query(vector=query_vector, top_k=top_k)

    return results
