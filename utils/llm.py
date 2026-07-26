import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found!")

client = genai.Client(api_key=api_key)

def summarize(chunk):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents = f"""
        You are an expert document summarizer.

        Summarize the following text into 5–7 concise bullet points.
        Keep only the important information.
        Do not include unnecessary details.

        Text:
        {chunk}
        """
    )
    return response.text
def final_summarize(all_summaries):
    combined_text = "\n\n".join(all_summaries)
    final_response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents = f"""
            You are an expert document summarizer.
    
            Summarize the following text into 5–7 concise bullet points.
            Keep only the important information.
            Do not include unnecessary details.
    
            Text:
            {combined_text}
            """
    )
    return final_response.text