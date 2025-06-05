import json, pathlib
import pandas as pd

def load_submissions(folder="data"):
    """Return a single DataFrame with all submission JSON files stacked."""
    rows = []
    for file in pathlib.Path(folder).glob("*.json"):
        with open(file) as f:
            blob = json.load(f)
        student = blob["student_id"]
        for rec in blob["records"]:
            rows.append({
                "student":    student,
                "subject":    rec["subject"],
                "chapter":    rec["chapter"],
                "concept":    rec.get("concept"),
                "difficulty": rec["difficulty"],
                "correct":    rec["correct"],
                "time":       rec["time_sec"]
            })
    df = pd.DataFrame(rows)
    return df
