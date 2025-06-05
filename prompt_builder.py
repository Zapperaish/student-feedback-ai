import textwrap, pandas as pd

INTRO_TMPL = """
You are a friendly teacher giving a personalised, motivating report.
Student raw metrics are below in JSON. 
Return **ONLY** a markdown report with these sections:

1. Personal intro (≤80 words, warm & human; refer to the student in second-person).
2. Performance Breakdown – bullet points for each subject ➜ chapter ➜ concept:
   * show accuracy (%) and avg time/question (s)
   * mark **Strength** if accuracy ≥80 %  OR **Focus Area** if <60 %
3. Time vs Accuracy Insights – 2–3 sentences.
4. Actionable Suggestions – exactly 3 numbered, each ≤25 words, specific.
"""

def build_prompt(student_df: pd.DataFrame) -> str:
    stats = (
        student_df
        .groupby(["subject", "chapter"])
        .agg(
            questions=("correct", "size"),
            accuracy =("correct", "mean"),
            avg_time =("time", "mean")
        )
        .reset_index()
    )
    payload = stats.to_dict(orient="records")
    
    prompt = INTRO_TMPL + "\n\nSTUDENT_DATA_JSON = ```json\n" + \
             textwrap.dedent(json.dumps(payload, indent=2)) + "\n```"
    return prompt
