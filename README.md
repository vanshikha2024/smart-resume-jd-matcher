# 🚀 Smart Resume-JD Matcher

An AI-powered web application that analyzes a candidate's resume against a Job Description (JD) and provides an intelligent compatibility analysis using Google Gemini.

The application helps job seekers understand how well their resume matches a specific role, identify missing skills, discover improvement areas, and get actionable recommendations.

---

## ✨ Features

- 📄 Upload Resume in PDF format
- 📝 Paste Resume text manually
- 💼 Paste Job Description
- 🤖 AI-powered analysis using Google Gemini
- 📊 Resume-JD Match Percentage
- ✅ Matching Skills Detection
- ⚠️ Missing Skills Detection
- 🎯 Candidate Strengths Analysis
- 📈 Skill Gap & Improvement Analysis
- 🚀 Actionable Recommendations
- 💻 Clean and responsive web interface
- 🔐 API key protected using environment variables

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **AI:** Google Gemini API
- **PDF Processing:** PyPDF
- **Environment Management:** python-dotenv

---

## 🧠 How It Works

The application follows a simple frontend-backend-AI workflow.

~~~text
User Resume (PDF / Text)
          +
    Job Description
          ↓
      Web Interface
     HTML / CSS / JS
          ↓
      Flask Backend
          ↓
   PDF Text Extraction
          ↓
     Google Gemini API
          ↓
     AI Resume Analysis
          ↓
    Structured JSON Result
          ↓
       Web Interface
          ↓
      Analysis Results
~~~

---

## 📁 Project Structure

~~~text
smart-resume-jd-matcher/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── templates/
    └── index.html
~~~

> **Note:** The `.env` file is created locally to store the Google Gemini API key and is excluded from GitHub using `.gitignore`.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

~~~bash
git clone https://github.com/vanshikha2024/smart-resume-jd-matcher.git
cd smart-resume-jd-matcher
~~~

### 2. Create a Virtual Environment

For Windows:

~~~bash
python -m venv venv
venv\Scripts\activate
~~~

For macOS/Linux:

~~~bash
python3 -m venv venv
source venv/bin/activate
~~~

### 3. Install Dependencies

~~~bash
pip install -r requirements.txt
~~~

The project uses:

- Flask
- python-dotenv
- google-genai
- pypdf

### 4. Configure Google Gemini API

Create a file named `.env` in the project root directory.

Add your Google Gemini API key:

~~~text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
~~~

> **Important:** Never share your API key or commit the `.env` file to GitHub.

### 5. Run the Application

~~~bash
python app.py
~~~

The application will start at:

~~~text
http://localhost:5000
~~~

Open the URL in your browser.

---

## 🖥️ How to Use

### Step 1 — Upload Resume

Upload your resume in PDF format.

The application automatically extracts the text from the uploaded PDF.

You can also paste your resume text manually.

### Step 2 — Enter Job Description

Paste the complete Job Description into the JD section.

### Step 3 — Analyze Resume

Click:

**✨ Analyze Match**

### Step 4 — View Results

The application displays an AI-generated analysis containing:

- Match Percentage
- Matching Skills
- Missing Skills
- Candidate Strengths
- Skill Gaps
- Improvement Areas
- Actionable Recommendations

---

## 📊 Analysis Provided

### Match Percentage

Provides an overall compatibility score between the candidate's resume and the Job Description.

### Matching Skills

Identifies skills that are present in both the resume and Job Description.

### Missing Skills

Identifies important skills mentioned in the Job Description that are not clearly present in the resume.

### Candidate Strengths

Highlights the candidate's relevant strengths based on the resume.

### Skill Gaps

Identifies areas where the candidate may need additional knowledge or experience.

### Improvement Suggestions

Provides suggestions for improving the candidate's profile.

### Actionable Recommendations

Provides practical recommendations that can help the candidate become better aligned with the target role.

---

## 💡 Example Use Case

A candidate can upload their resume and compare it with a job posting.

### Resume

~~~text
Python, JavaScript, React, Node.js, SQL
~~~

### Job Description

~~~text
Python, React, Node.js, AWS, Docker, Kubernetes
~~~

### Possible Analysis

**Matching Skills**

- Python
- React
- Node.js

**Missing Skills**

- AWS
- Docker
- Kubernetes

**Improvement Area**

Gain hands-on experience with cloud computing and containerization technologies.

This allows candidates to understand their strengths and skill gaps before applying.

---

## 🔌 API Endpoints

### `/`

Loads the main web application.

### `/analyze`

Accepts the resume and Job Description and generates the AI-powered analysis.

It supports:

- Resume text input
- PDF resume upload
- Job Description input

### `/health`

Provides a simple health check for the application.

---

## 🤖 Google Gemini Integration

The application uses the Google Gemini API to perform intelligent resume analysis.

The Flask backend sends the resume and Job Description to Gemini using a structured prompt.

Gemini analyzes the provided information and returns structured JSON containing the required analysis fields.

The backend then sends the structured result to the frontend, where it is displayed to the user.

---

## 🔐 Security

The Google Gemini API key is stored in an environment variable instead of being written directly inside the Python source code.

The `.env` file is excluded from Git using `.gitignore`.

Never commit or share:

~~~text
.env
~~~

Never expose your Gemini API key publicly.

---

## 🧪 Error Handling

The application handles common issues such as:

- Missing resume
- Missing Job Description
- Invalid file type
- Empty PDF
- Large PDF uploads
- Invalid API responses
- Temporary Gemini API errors
- Invalid JSON responses

This helps make the application more reliable when invalid input or temporary API issues occur.

---

## 🎯 Problem Solved

Job seekers often apply to positions without knowing how closely their resume matches the requirements of a role.

Manually comparing a resume with every Job Description can be time-consuming.

This project provides an AI-assisted solution to:

- Understand job compatibility
- Identify matching skills
- Identify missing skills
- Discover resume gaps
- Prioritize learning areas
- Improve career preparation
- Make more informed job applications

---

## 🌟 Benefits

### For Students

- Understand whether their resume matches a job
- Identify skills they need to learn
- Prepare better before placement drives
- Improve their resume according to specific roles

### For Job Seekers

- Quickly compare resumes with different jobs
- Identify missing requirements
- Understand strengths and weaknesses
- Get actionable improvement suggestions

---

## 🚀 Future Improvements

- 📌 ATS compatibility score
- 📌 Resume keyword optimization
- 📌 Automatic Job Description keyword extraction
- 📌 Resume improvement suggestions
- 📌 Multiple job comparison
- 📌 Job recommendation system
- 📌 Resume version management
- 📌 User authentication
- 📌 Cloud deployment
- 📌 Resume analytics dashboard
- 📌 Resume scoring history
- 📌 Job-specific resume generation
- 📌 Interview preparation based on Job Description

---

## 📚 Key Learning Outcomes

Through this project, the following concepts were implemented:

- Flask REST API development
- Frontend-backend integration
- Google Gemini API integration
- Generative AI prompting
- Structured JSON generation
- PDF text extraction
- File upload handling
- Environment variable management
- Error handling
- Responsive web UI
- API integration
- JSON data processing
- Basic web application architecture

---

## 🏗️ Application Architecture

~~~text
             FRONTEND
          HTML / CSS / JS
                │
                │
       Resume + Job Description
                │
                ▼
         FLASK BACKEND
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
 PDF Text Extraction  Input Validation
        │                │
        └───────┬────────┘
                │
                ▼
       GOOGLE GEMINI API
                │
                ▼
       STRUCTURED ANALYSIS
                │
                ▼
         FLASK BACKEND
                │
                ▼
        FRONTEND RESULTS
~~~

---

## 📦 Requirements

The application requires Python and the following packages:

~~~text
flask==3.0.0
python-dotenv==1.0.0
google-genai
pypdf
~~~

All dependencies are included in `requirements.txt`.

Install them using:

~~~bash
pip install -r requirements.txt
~~~

---

## 📌 Important Notes

- Python must be installed on your system.
- A valid Google Gemini API key is required.
- The API key must be stored inside `.env`.
- Do not upload `.env` to GitHub.
- Resume files should be in PDF format when using the upload option.
- Internet access is required for Gemini API analysis.
- The application runs locally using Flask.

---

## 👩‍💻 Author

**Vanshikha Singh**

GitHub: https://github.com/vanshikha2024

---

## ⭐ Project Summary

**Smart Resume-JD Matcher** combines web development, backend programming, PDF processing, and Generative AI to create an intelligent resume analysis tool.

The project demonstrates how a Flask-based web application can integrate with a Generative AI API to process real-world career-related data and provide useful, structured insights to users.

---

## 🔒 License

This project is created for educational and portfolio purposes.
