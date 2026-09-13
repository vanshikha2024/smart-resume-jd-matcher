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
- 📈 Gap & Improvement Analysis
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

```text
User Resume (PDF / Text)
          +
    Job Description
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

📁 Project Structure
smart-resume-jd-matcher/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── templates/
    └── index.html

⚙️ Installation & Setup
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd smart-resume-jd-matcher
2. Install Dependencies
pip install -r requirements.txt
3. Create Environment File

Create a file named:

.env

Add your Google Gemini API key:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

Never share your API key or commit the .env file to GitHub.

4. Run the Application
python app.py

The application will start at:

http://localhost:5000

Open the URL in your browser.

🧪 How to Use
Step 1

Upload your resume as a PDF.

You can also paste your resume text manually.

Step 2

Paste the Job Description into the JD section.

Step 3

Click:

✨ Analyze Match
Step 4

The application sends the resume and JD to Google Gemini and displays the AI-generated analysis.

💡 Example Use Case

A candidate can upload their resume and compare it with a job posting.

For example:

Resume:
Python, JavaScript, React, Node.js, SQL

Job Description:
Python, React, Node.js, AWS, Docker, Kubernetes

The application can identify:

Matching Skills:
Python
React
Node.js

Missing Skills:
AWS
Docker
Kubernetes

Improvement:
Gain hands-on experience with cloud and containerization technologies.

This allows candidates to understand their strengths and skill gaps before applying.

🎯 Problem Solved

Job seekers often apply to positions without knowing how closely their resume matches the requirements.

This project provides an AI-assisted way to:

Understand job compatibility
Identify missing skills
Discover resume gaps
Prioritize learning areas
Make more informed job applications
🚀 Future Improvements
📌 ATS compatibility score
📌 Resume keyword optimization
📌 Automatic JD keyword extraction
📌 Resume improvement suggestions
📌 Multiple job comparison
📌 Job recommendation system
📌 Resume version management
📌 User authentication
📌 Cloud deployment
📌 Resume analytics dashboard
📌 Key Learning Outcomes

Through this project, the following concepts were implemented:

Flask REST API development
Frontend-backend integration
Google Gemini API integration
Generative AI prompting
Structured JSON generation
PDF text extraction
File upload handling
Environment variable management
Error handling
Responsive web UI
👩‍💻 Author

Vanshikha Singh