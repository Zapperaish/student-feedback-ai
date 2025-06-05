import pandas as pd, argparse, pathlib
from data_loader import load_submissions
from feedback_generator import generate_markdown
from pdf_generator import md_to_pdf

def run(data_dir, output):
    df = load_submissions(data_dir)
    report_md = generate_markdown(df)
    pdf_path  = md_to_pdf(report_md, output)
    print(f"✅ PDF created → {pdf_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-d","--data",  default="data", help="folder with JSON files")
    ap.add_argument("-o","--out",   default="student_report.pdf", help="PDF name")
    args = ap.parse_args()
    pathlib.Path(args.data).mkdir(exist_ok=True)
    run(args.data, args.out)
