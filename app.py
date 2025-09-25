from flask import Flask, request, render_template
import os
import docx2txt
import PyPDF2
from utils.summarizer import summarize_text
from utils.entity_extractor import extract_entities

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    uploaded_file = request.files["document"]

    if uploaded_file.filename != "":
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(file_path)

        # Extract text depending on file type
        if uploaded_file.filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        elif uploaded_file.filename.endswith(".docx"):
            text = docx2txt.process(file_path)
        elif uploaded_file.filename.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(open(file_path, "rb"))
            text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        else:
            return "Unsupported file format!"

        # Summarization + entity extraction
        summary = summarize_text(text)
        entities = extract_entities(text)

        return render_template("result.html", summary=summary, entities=entities)

    return "No file uploaded!"

if __name__ == "__main__":
    app.run(debug=True)
