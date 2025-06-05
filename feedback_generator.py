import openai, os, dotenv
from prompt_builder import build_prompt

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_markdown(df):
    prompt = build_prompt(df)
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    return resp.choices[0].message.content.strip()
