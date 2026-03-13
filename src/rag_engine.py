from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, index, chunks):

    q_emb = model.encode([query])

    D, I = index.search(np.array(q_emb), 3)

    results = []

    for i in I[0]:
        results.append(chunks[i])

    return results
