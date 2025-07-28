## Approach Explanation

We developed a generic CPU-based intelligent document processor that supports various personas and document types. The system works in three steps:
1. **Text Extraction** using PyMuPDF for speed and reliability.
2. **Relevance Scoring** using Sentence-BERT embeddings to match content with the persona + job intent.
3. **Ranking** based on semantic similarity and generating JSON output in the required format.

Our model is under 1GB (MiniLM-L6-v2) and can process 3–5 documents in under 60 seconds.
