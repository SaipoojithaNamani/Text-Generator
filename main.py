import os
from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
generative_configure = {
    "max_output_tokens" : 100
}
app = FastAPI()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest", generation_config=generative_configure)
@app.post("/")
async def quote_generator():
    try:
        prompt = ("Who is the founder of Malla Reddy University?")
        response = model.generate_content(prompt)
        if not response:
            raise ValueError("You are getting empty result")
        return {"quote": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        
        



