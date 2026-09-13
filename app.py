"""
Smart Resume-JD Matcher using Google Gemini
Supports PDF resume upload and manual resume text input.
"""

from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
from pypdf import PdfReader
import os
from dotenv import load_dotenv
import json


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )


# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)

# Maximum uploaded file size = 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


# ==========================================
# GEMINI CONFIGURATION
# ==========================================

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.8-flash"


# ==========================================
# PDF TEXT EXTRACTION
# ==========================================

def extract_text_from_pdf(pdf_file):
    """
    Extract text from an uploaded PDF resume.
    """

    try:
        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:
        raise Exception(f"Could not read PDF: {str(e)}")


# ==========================================
# GEMINI RESUME ANALYSIS
# ==========================================

def analyze_resume_jd_match(resume_text, jd_text):

    prompt = f"""
You are an expert HR analyst and technical recruiter.

Analyze the following resume against the job description.

JOB DESCRIPTION:
{jd_text}

RESUME:
{resume_text}

Evaluate the candidate objectively.

Return ONLY valid JSON with exactly these fields:

{{
    "match_percentage": 0,
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "gaps": [],
    "improvements": [],
    "technical_fit": "",
    "soft_skills_fit": "",
    "overall_verdict": "",
    "key_message": ""
}}

Rules:

1. match_percentage must be a realistic number between 0 and 100.

2. matching_skills should contain 5-7 relevant skills
   from the resume that match the JD.

3. missing_skills should contain 3-5 important skills
   from the JD that are missing from the resume.

4. strengths should contain 2-3 strong points about the candidate.

5. gaps should contain 2-3 important gaps.

6. improvements should contain 3-4 actionable recommendations.

7. technical_fit should be one short sentence.

8. soft_skills_fit should be one short sentence.

9. overall_verdict must be exactly one of:
   "Strong Match"
   "Good Match"
   "Moderate Match"
   "Needs Improvement"

10. key_message should be one concise sentence.

11. Do not add markdown.

12. Do not add ```json.

13. Base the analysis only on the provided resume and JD.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )

        response_text = response.text.strip()

        analysis = json.loads(response_text)

        return {
            "success": True,
            "data": analysis,
            "error": None
        }

    except json.JSONDecodeError as e:

        return {
            "success": False,
            "data": None,
            "error": f"Failed to parse AI response: {str(e)}"
        }

    except Exception as e:

        return {
            "success": False,
            "data": None,
            "error": f"Gemini API Error: {str(e)}"
        }


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# ANALYZE ENDPOINT
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        # --------------------------------------
        # CASE 1: PDF UPLOAD
        # --------------------------------------

        if "resume_file" in request.files:

            resume_file = request.files["resume_file"]

            if resume_file and resume_file.filename:

                if not resume_file.filename.lower().endswith(".pdf"):
                    return jsonify({
                        "success": False,
                        "error": "Please upload a PDF file."
                    }), 400

                resume = extract_text_from_pdf(resume_file)

            else:
                resume = ""


        # --------------------------------------
        # CASE 2: MANUAL TEXT INPUT
        # --------------------------------------

        else:

            data = request.get_json()

            resume = data.get("resume", "").strip()


        # --------------------------------------
        # GET JOB DESCRIPTION
        # --------------------------------------

        if request.files:

            jd = request.form.get("jd", "").strip()

        else:

            data = request.get_json()

            jd = data.get("jd", "").strip()


        # --------------------------------------
        # VALIDATION
        # --------------------------------------

        if not resume:

            return jsonify({
                "success": False,
                "error": "Please upload a resume PDF or paste your resume text."
            }), 400

        if not jd:

            return jsonify({
                "success": False,
                "error": "Please enter the job description."
            }), 400

        # --------------------------------------
        # GEMINI ANALYSIS
        # --------------------------------------

        result = analyze_resume_jd_match(
            resume,
            jd
        )

        return jsonify(result)


    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "ok",
        "service": "Resume Matcher API"
    }), 200


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":

    print("🚀 Smart Resume-JD Matcher is starting...")
    print("📍 Open http://localhost:5000 in your browser")
    print("💡 Press Ctrl+C to stop the server")

    app.run(
        debug=True,
        port=5000
    )