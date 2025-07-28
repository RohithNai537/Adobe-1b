import json
from datetime import datetime

def get_timestamp():
    return datetime.now().isoformat()

def load_persona_job(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data['persona'], data['job_to_be_done']
