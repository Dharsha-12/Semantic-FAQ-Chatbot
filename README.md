# Semantic FAQ Chatbot

A beginner-friendly AI project that demonstrates **semantic search** using **Sentence Transformers** and **ChromaDB**.

Instead of matching exact keywords, the chatbot understands the meaning behind a user's question and retrieves the most relevant answer from a FAQ knowledge base using vector similarity search.

---

## 🚀 Features

- Semantic search using text embeddings
- Vector storage with ChromaDB
- Retrieves answers based on meaning, not exact keywords
- Interactive terminal-based chatbot
- Beginner-friendly project structure
- No LangChain required
- Demonstrates the retrieval component of RAG

---

## 📁 Project Structure

```text
.
├── faq_data.py         # FAQ questions and answers
├── store_embeddings.py # Creates embeddings and saves them in ChromaDB
├── search.py           # Asks questions and searches for the closest FAQ
└── requirements.txt    # Project dependencies
```

---

## ⚙️ Requirements

- Python 3.9+
- Internet connection (only required the first time to install dependencies and download the embedding model)

---

## 🛠 Installation

Open a terminal in the project folder.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## ▶ Running the Chatbot

Run these commands in order:

```bash
python store_embeddings.py
python search.py
```

### What happens?

**store_embeddings.py**

- Loads all FAQ questions.
- Generates embeddings using Sentence Transformers.
- Stores them in ChromaDB.

**search.py**

- Accepts a user question.
- Converts it into an embedding.
- Searches ChromaDB for the closest FAQ.
- Returns the most relevant answer.

> You only need to run `store_embeddings.py` again if you modify the FAQs.

---

## 💬 Example

```text
FAQ chatbot is ready. Type 'quit' or 'exit' to stop.

Your question:
How do I make a Python list?

Closest FAQ:
How do I create a list in Python?

Answer:
Use square brackets, for example:
colors = ['red', 'blue']

Similarity score (cosine similarity):
0.7
```

*The similarity score above is only an example. Actual scores may vary depending on the question and embedding model.*

---

## 📚 Example Questions

The included FAQ dataset covers topics such as:

- What is a variable in Python?
- How do I create a list in Python?
- What is a Python dictionary?
- How do I define a function in Python?
- What is a loop used for?
- What is the difference between a list and a tuple?
- How can I install a Python package?
- What does an if statement do?
- What is a Python module?
- How do I handle errors in Python?
- What does the return statement do?
- What is a virtual environment?

You can phrase questions in different ways. The chatbot searches for the closest semantic match rather than requiring exact wording.

---

## 🧠 How It Works

### Step 1: FAQ Data

`faq_data.py` contains a list of frequently asked questions and answers.

### Step 2: Generate Embeddings

`store_embeddings.py` uses the **all-MiniLM-L6-v2** model from Sentence Transformers to convert each FAQ question into a vector embedding.

### Step 3: Store in ChromaDB

Each question embedding, along with its answer, is stored inside ChromaDB.

### Step 4: Ask a Question

The user's question is converted into an embedding using the same model.

### Step 5: Similarity Search

ChromaDB compares the new embedding against stored embeddings and returns the closest match.

### Step 6: Display the Answer

The chatbot shows:

- Closest FAQ
- Answer
- Similarity score

---

## 🔄 Workflow Diagram

```text
FAQ Questions
      │
      ▼
Embedding Model
      │
      ▼
ChromaDB Vector Store
      ▲
      │
      │ Similarity Search
      │
User Question
      │
      ▼
Embedding Model
      │
      ▼
Closest Match Found
      │
      ▼
FAQ Answer + Similarity Score
```

---

## 📖 Key Concepts

### Embeddings

An embedding is a numerical representation of text.

Example:

```text
"I want to learn stitching."

"I want to learn tailoring."
```

Even though the words differ, embeddings place these sentences close together because they have similar meanings.

---

### Vector Database

ChromaDB stores embeddings and enables fast similarity searches.

This project uses a local persistent database stored in:

```text
chroma_db/
```

---

### Similarity Search

When the user asks a question, the chatbot compares its embedding with stored FAQ embeddings.

The closest match is returned based on cosine similarity.

```text
Cosine Similarity = 1 - Cosine Distance
```

A higher score indicates a stronger semantic match.

---

### Retrieval-Augmented Generation (RAG)

This project demonstrates the **retrieval** portion of a RAG system.

Current flow:

```text
Question
   ↓
Retrieve Relevant FAQ
   ↓
Return Answer
```

A complete RAG system would extend this by:

```text
Question
   ↓
Retrieve Relevant Information
   ↓
Send Context to LLM
   ↓
Generate Final Response
```

---

## ✏️ Adding or Modifying FAQs

Edit the `FAQS` list inside:

```python
faq_data.py
```

After making changes:

```bash
python store_embeddings.py
```

Then restart the chatbot:

```bash
python search.py
```

---

## 📦 Dependencies

### sentence-transformers

Generates text embeddings using:

```text
all-MiniLM-L6-v2
```

### chromadb

Stores embeddings and performs similarity search.

---

## 🎯 Learning Objectives

By completing this project, you will learn:

- What embeddings are
- How semantic search works
- How vector databases store data
- How similarity search is performed
- The retrieval stage of RAG systems
- Building AI applications with Python

---

## 🚀 Future Improvements

- Add PDF document support
- Create a complete RAG pipeline
- Integrate Gemini API
- Build a Streamlit web interface
- Support multiple document collections
- Add conversation history
- Add multiple similarity search options

---

## 👨‍💻 Author

**Dharsha**

Second-year Computer Science student specialising in Cyber Security, exploring AI, Vector Databases, RAG, and Machine Learning through hands-on projects.

---

## ⭐ Star the Repository

If you found this project helpful, consider giving it a star and following the project as it evolves into a complete RAG chatbot.
