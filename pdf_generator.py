import tempfile, weasyprint, markdown

CSS = """
h1,h2 { font-family: Poppins, sans-serif; }
strong { color:#1b87f5; }
"""

def md_to_pdf(md_text, out_path="report.pdf"):
    html = markdown.markdown(md_text, extensions=["markdown.extensions.tables"])
    html_full = f"<style>{CSS}</style>" + html
    weasyprint.HTML(string=html_full).write_pdf(out_path)
    return out_path
