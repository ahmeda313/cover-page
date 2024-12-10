from docx import Document

def extract_text(file_path):
    """Extract text from a .docx file."""
    doc = Document(file_path)
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    return text

