# student-feedback-ai

AI-Powered Student Performance Feedback ✨

 🏗 Tech Stack
 Python 3.11
 OpenAI GPT-4o-mini
 pandas | matplotlib | Jinja2 | WeasyPrint

 🚀 How It Works
1. Data Processing  
   `data_loader.py` merges all `.json` submissions and computes per-chapter stats.

2. Prompt Logic (`prompt_builder.py`)  
   Packs clean JSON + explicit markdown layout instructions to force a structured, human-sounding answer.

3. LLM Call (`feedback_generator.py`)  
   One-shot ChatCompletion; temperature 0.7 for mild creativity.

4. PDF Generation (`pdf_generator.py`)  
   Markdown → HTML → styled PDF via WeasyPrint.

 📄 Report Structure
1. Personalised intro  
2. Subject → Chapter breakdown with strengths & focus areas  
3. Time vs. accuracy narrative  
4. Three concrete tips  

 🏁 Quick Start
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # add your OpenAI key
python main.py -d data -o report.pdf
