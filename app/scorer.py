from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("all-MiniLM-L6-v2")  # ~80MB, fast and CPU-friendly

def rank_sections(docs_data, persona, job):
    query = f"{persona}. Task: {job}"
    query_emb = model.encode(query, convert_to_tensor=True)

    results = []
    subresults = []

    for doc, pages in docs_data.items():
        for page in pages:
            section_text = page['text']
            section_emb = model.encode(section_text, convert_to_tensor=True)
            score = float(util.pytorch_cos_sim(query_emb, section_emb))

            results.append({
                "document": doc,
                "page_number": page['page_number'],
                "section_title": section_text.strip().split('\n')[0][:100],
                "importance_rank": score
            })

            subresults.append({
                "document": doc,
                "page_number": page['page_number'],
                "refined_text": section_text[:500]  # Top 500 chars
            })

    # Sort and rank
    sorted_sections = sorted(results, key=lambda x: x["importance_rank"], reverse=True)[:10]
    for i, s in enumerate(sorted_sections):
        s["importance_rank"] = i + 1

    return {
        "sections": sorted_sections,
        "subsections": subresults[:10]
    }
