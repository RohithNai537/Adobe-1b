from app.processor import process_documents
from app.utils import get_timestamp, load_persona_job

if __name__ == "__main__":
    docs_path = "data/sample_docs/"
    persona, job = load_persona_job("data/persona_job.json")
    output = process_documents(docs_path, persona, job)
    timestamp = get_timestamp()
    output['metadata']['processing_timestamp'] = timestamp

    # Save to output
    import json
    with open("output/challenge1b_output.json", "w") as f:
        json.dump(output, f, indent=4)
