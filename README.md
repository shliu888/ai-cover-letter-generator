

# 💼 AI Cover Letter & Resume Matcher

## ✨ Project Overview: The Smart Hired Coach

The **AI Cover Letter & Resume Matcher** is a powerful, yet minimalist, application designed to instantly evaluate a candidate's documents against a specific Job Description (JD). Built to eliminate guesswork and maximize interview chances, it provides actionable, data-driven feedback across three key dimensions: **Skill Match, Confidence Tone, and Role Alignment.**

This project demonstrates core skills in modern LLM application development, including prompt engineering, structured output generation, and agentic workflow orchestration using LangChain/LangGraph.

-----

## 🚀 Key Features and Impact

| Feature | Description | Resume Bonus Highlight |
| :--- | :--- | :--- |
| **Skill Match Scoring** | Quantifies the resume's alignment by scoring how many mandatory JD keywords are *explicitly* present. | **Structured Output:** Forces the LLM to return a clean percentage score and a list of missing terms. |
| **Sentiment Analysis** | Evaluates the tone of the cover letter/resume across **Confidence**, **Clarity**, and **Professionalism** (1-10 scores). | **Advanced Prompt Engineering:** Guides the LLM to perform nuanced, subjective qualitative analysis. |
| **Role Alignment Summary** | Generates a single-sentence summary of the biggest thematic disconnect between the candidate's history and the job requirements. | **Agentic Reasoning:** Shows the model acting as a domain expert (a Hiring Manager). |

-----

## 🛠️ Technology Stack

This project leverages the modern LLM application stack for rapid development and high intelligence.

  * **Orchestration:** **LangChain / LangGraph** (for chaining LLM calls and state management)
  * **Core AI:** **Google Gemini API** (via `langchain-google-genai`)
  * **Environment:** Python 3.9+

-----

## ⚙️ Installation and Setup

### 1\. Clone the Repository

```bash
git clone [YOUR_REPO_LINK]
cd ai-resume-matcher
```

### 2\. Set Up the Environment

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

*(Note: You will need to create a `requirements.txt` file listing all libraries used, like `langchain-google-genai`, `langchain`, `langgraph`, `gradio`, `python-dotenv`.)*

### 3\. API Key Configuration

Create a file named `.env` in the project root directory and add your key:

```
# Get your key from Google AI Studio or Google Cloud
GOOGLE_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
```

-----

## ▶️ How to Run

Execute the main application file:

```bash
python [YOUR_MAIN_FILE_NAME].py
```
  * **PDF/DOCX Upload:** Implement a file handler to accept document uploads instead of just text input.
  * **Feedback Iteration Node:** Use LangGraph to create a loop where the generated feedback is immediately used to suggest revisions to the user's text.
  * **Role-Specific Fine-Tuning:** Use few-shot examples to specialize the prompt for specific domains (e.g., Software Engineering, Marketing).
