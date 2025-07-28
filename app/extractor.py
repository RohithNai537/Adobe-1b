import fitz  # PyMuPDF
import os

def extract_sections(folder_path):
    docs_data = {}
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            doc = fitz.open(os.path.join(folder_path, file))
            pages = []
            for i, page in enumerate(doc):
                text = page.get_text()
                if len(text.strip()) > 100:
                    pages.append({
                        "document": file,
                        "page_number": i + 1,
                        "text": text
                    })
            docs_data[file] = pages
    return docs_data
