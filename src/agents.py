import os
import json
import google.generativeai as genai # <--- CHANGED to standard import
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# --- CONFIGURATION (STABLE SDK) ---
genai.configure(api_key=api_key)
MODEL_ID = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_ID)

def log_event(session_logs, agent_name, action, details):
    """Simple Observability: Tracks what agents are doing."""
    entry = {
        "agent": agent_name,
        "action": action,
        "details": details
    }
    session_logs.append(entry)
    return entry

def run_agent_pipeline(analysis_result, session_logs):
    """
    Runs the Detective -> Editor -> Strategist pipeline.
    """
    
    # --- AGENT 1: DETECTIVE (Data Analysis) ---
    # The 'Tool' runs deterministically first (passed in via analysis_result)
    log_event(session_logs, "Detective", "TOOL_USE", f"Analyzed CSV. Found anomaly in {analysis_result.get('month')}")
    
    # --- AGENT 2: EDITOR (Narrative Generation) ---
    log_event(session_logs, "Editor", "THINKING", "Drafting news story based on data...")
    
    editor_prompt = f"""
    You are a Senior Data Journalist.
    DATA: {json.dumps(analysis_result)}
    
    Write a short 'Breaking News' style internal memo (max 100 words).
    - HEADLINE: Catchy and Urgent.
    - BODY: Explain the dip in revenue vs the average.
    """
    
    # STABLE API CALL
    response_editor = model.generate_content(editor_prompt)
    article_text = response_editor.text
    
    log_event(session_logs, "Editor", "OUTPUT", article_text[:50] + "...")

    # --- AGENT 3: STRATEGIST (Action Plan) ---
    log_event(session_logs, "Strategist", "THINKING", "Analyzing article for strategic risks...")
    
    strategist_prompt = f"""
    Based on this news brief: "{article_text}"
    
    Provide 3 bullet points of IMMEDIATE ACTION for the CEO.
    Keep it strictly business-focused.
    """
    
    # STABLE API CALL
    response_strat = model.generate_content(strategist_prompt)
    
    log_event(session_logs, "Strategist", "OUTPUT", "Generated 3 strategic points.")
    
    return {
        "article": article_text,
        "strategy": response_strat.text
    }