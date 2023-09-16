import os
from PyPDF2 import PdfReader
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import openai
from dotenv import load_dotenv
import os
import io

load_dotenv()

app = Flask(__name__)
openai.api_key = os.environ.get("OPEN_AI_API_KEY")

def extract_pdf_text(file):
    pdf_data = io.BytesIO(file.read())
    pdf_reader = PdfReader(pdf_data)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_job_description_text(file):
    text = file.read().decode('utf-8')
    return text

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_message', methods=['POST'])
def generate_message():
    resume = request.files['resume.pdf']
    job_description = request.files['job_description.txt']

    resume_text = extract_pdf_text(resume)
    job_description_text = extract_job_description_text(job_description)

    prompt = f"In < 150 tokens, generate a personalized message for a potential job candidate based strictly on the intersection between the following resume and job description: {resume_text} {job_description_text}. Generate a personalized yet concise message informing the candidate that his or her skills are sought after by Albedo, whose mission is to redefine current standards of satellite imagery and subsequent fields. Ensure the message is complete and includes a closing salutation."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=["Looking forward to hearing from you,"],
        temperature=0.35,
    )

    message = response.choices[0].text.strip()
    return render_template('results.html', message=message)

if __name__ == "__main__":
    app.run()