# 🇧🇩 AI Study Buddy

**AI Study Buddy** is a smart, AI-powered educational assistant tailored for Bangladeshi students. It explains complex topics in simple Bengali, provides relatable local examples (like rickshaws, cricket, tea stalls), and generates formatted study notes.

🔗 **Live Demo:** https://aistudy-buddy.streamlit.app/

---

## Features
- **Simple Definitions:** Explains tough concepts in easy Bengali.
- **Context-Aware Examples:** Automatically selects the best Bangladeshi scenario (e.g., Village life, Eid shopping) instead of generic examples.
- **Smart Formatting:** Generates organized notes with bullet points and tables.
- **Mobile Friendly:** Optimized for viewing on mobile devices.
- **Downloadable Notes:** One-click download for the study notes as HTML files.

## Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM (Brain):** Google Gemini 2.0 Flash
- **Search Tool:** Tavily API
- **Framework:** LangChain & LangGraph

## 📂 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mdshafiulalamsagar/ai-study-buddy.git](https://github.com/YOUR_USERNAME/ai-study-buddy.git)
   cd ai-study-buddy
   pip install -r requirements.txt
   GEMINI_API_KEY="your_gemini_key"
   TAVILY_API_KEY="your_tavily_key"
   streamlit run app.py
