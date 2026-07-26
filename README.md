# 📄 AI PDF Summarizer

An AI-powered PDF summarizer built with **Python**, **PyMuPDF**, and **Google Gemini API**. The application extracts text from PDF documents, processes large files by splitting them into manageable chunks, summarizes each chunk using Gemini, and then generates one concise final summary.

---

## 🚀 Features

- 📖 Read and extract text from PDF files
- 🧹 Clean and preprocess extracted text
- ✂️ Split large documents into chunks
- 🤖 Generate summaries for each chunk using Google Gemini
- 📝 Combine chunk summaries into one final summary
- 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- PyMuPDF (Fitz)
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
AI-PDF-Summarizer/
│
├── pdfs/
│   └── document_2.pdf
│
├── utils/
│   ├── pdf_reader.py
│   ├── text_cleaner.py
│   ├── chunker.py
│   └── llm.py
│
├── output/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env (not included)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abhisheksen777/AI-PDF-Summarizer.git
```

### 2. Move into the project

```bash
cd AI-PDF-Summarizer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 6. Run the project

```bash
python main.py
```

---

## 🔄 Workflow

```
PDF
 │
 ▼
Read PDF
 │
 ▼
Extract Text
 │
 ▼
Clean Text
 │
 ▼
Split into Chunks
 │
 ▼
Summarize Each Chunk
 │
 ▼
Merge Chunk Summaries
 │
 ▼
Generate Final Summary
```

---

## 📸 Sample Output

```
===== FINAL SUMMARY =====

• AI and NLP enable automatic document summarization.
• Machine Learning powers Large Language Models.
• The project extracts, cleans, chunks, and summarizes PDFs.
• Hierarchical summarization improves long-document handling.
• The sample document is designed for testing PDF processing.
```

---

## 📌 Future Improvements

- Streamlit Web Interface
- Upload any PDF through the UI
- Export summaries to TXT/PDF
- Support multiple summary styles
- Better error handling and retry mechanism
- Support multiple LLM providers

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abhishek Sen**

GitHub: https://github.com/abhisheksen777
