# Text-Generator
# Simple GenAI API (FastAPI + Gemini)

This is a **very basic Generative AI project** created for learning purposes. It demonstrates how to connect **Google Gemini API** with **FastAPI** and test the response using **Thunder Client**.



## 📌 What I Did 

* Created a **separate Python virtual environment (venv)**
* Created a single Python file (`main.py`)
* Generated a **Gemini API key** from **Google AI Studio**
* Used **FastAPI** to create an API
* Tested the API using **Thunder Client** in VS Code




## 🛠 Tools & Technologies Used

* Python
* FastAPI
* Google Generative AI (Gemini)
* Thunder Client (VS Code extension)
* Virtual Environment (venv)


## 📁 Project Files

```
project-folder/
│
├── main.py
├── .env
└── venv/
```



## 🔐 API Key Setup

1. Go to **Google AI Studio**
2. Generate a Gemini API key
3. Create a `.env` file
4. Add your key:

```
GEMINI_API_KEY=your_api_key_here
```



## ▶️ How to Run the Project

Activate virtual environment:

```bash
venv\Scripts\activate   # Windows
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```


## 🔁 API Testing (Thunder Client)

* Method: **POST**
* URL:

  ```
  http://127.0.0.1:8000/ask
  ```
* Headers:

  ```
  Content-Type: application/json
  ```
* Body: **Not required**



## 📤 Sample Output

```json
{
  "answer": "The founder of Malla Reddy University is Shri Malla Reddy."
}
```



r learning Generative AI fundamentals.
