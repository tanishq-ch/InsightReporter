import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Client
client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.0-flash-exp"

def run_agent_pipeline(analysis_result, session_history):
    """
    Orchestrates the 3-Agent Flow.
    Args:
        analysis_result (dict): The data found by the Tool.
        session_history (list): A list to append logs to.
    Returns:
        dict: Contains the 'article' and 'strategy' text.
    """
    
    # --- AGENT 1: The Detective (Already ran via tools.py) ---
    # In this architecture, the 'Tool' is triggered by the UI, passed to the Agents.
    session_history.append({"role": "Detective", "content": f"Anomaly Detected: {analysis_result}"})

    # --- AGENT 2: The Editor ---
    editor_prompt = f"""
    You are a Senior Data Journalist. 
    DATA ANOMALY FOUND: {analysis_result}
    
    Write a 'Breaking News' style brief (max 150 words).
    - Headline: Dramatic and professional.
    - Body: Compare the specific month's data to the averages provided.
    - Tone: Urgent business intelligence.
    """
    
    response_editor = client.models.generate_content(
        model=MODEL_ID, contents=editor_prompt
    )
    article_text = response_editor.text
    session_history.append({"role": "Editor", "content": article_text})

    # --- AGENT 3: The Strategist ---
    strategist_prompt = f"""
    Read this internal news brief: 
    "{article_text}"
    
    Suggest 3 specific, actionable bullet points for the CEO to fix this.
    """
    
    response_strat = client.models.generate_content(
        model=MODEL_ID, contents=strategist_prompt
    )
    strategy_text = response_strat.text
    session_history.append({"role": "Strategist", "content": strategy_text})
    
    return {
        "article": article_text,
        "strategy": strategy_text
    }