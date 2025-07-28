from app.extractor import extract_sections
from app.scorer import rank_sections

def process_documents(doc_folder, persona, job):
    extracted_sections = extract_sections(doc_folder)
    ranked_sections = rank_sections(extracted_sections, persona, job)
    output = {
        "metadata": {
            "input_documents": list(extracted_sections.keys()),
            "persona": persona,
            "job_to_be_done": job
        },
        "extracted_sections": ranked_sections["sections"],
        "sub_section_analysis": ranked_sections["subsections"]
    }
    return output
