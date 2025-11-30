import streamlit as st
import pandas as pd
import plotly.express as px
from src.tools import get_sales_data, analyze_worst_month
from src.agents import run_agent_pipeline
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="InsightReporter", page_icon="📰", layout="wide")

# --- HEADER ---
st.title("📰 InsightReporter")
st.markdown("**The AI-Powered Data Newsroom for Enterprise**")
st.markdown("---")

# --- SIDEBAR (Controls) ---
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🔄 Generate/Reset Mock Data"):
        # Run the generator inline
        from data_generator import create_dummy_data
        create_dummy_data()
        st.success("New data generated!")
        st.rerun()

# --- MAIN APP LOGIC ---

# 1. Load Data
df, error = get_sales_data()

if error:
    st.warning("⚠️ No data found. Click 'Generate Mock Data' in the sidebar.")
else:
    # Layout: Data on Left, Agents on Right
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📊 Raw Enterprise Data")
        st.dataframe(df, use_container_width=True)
        
        # Chart
        st.subheader("Visual Analysis")
        fig = px.line(df, x='Month', y=['Revenue_Millions', 'Churn_Rate'], 
                      title="Revenue vs Churn Trends")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🤖 AI Agent Newsroom")
        
        if st.button("🚀 Launch Investigation", type="primary"):
            
            # SESSION STATE (Memory)
            if 'history' not in st.session_state:
                st.session_state['history'] = []

            # Step 1: Tool Execution
            with st.status("🕵️‍♂️ Agent 1 (Detective): Scanning Database...", expanded=True) as status:
                analysis = analyze_worst_month(df)
                st.write(f"**Anomaly Found:** Month of {analysis['month']}")
                st.write(f"Churn Rate: {analysis['churn']} (Avg: {analysis['avg_churn']})")
                status.update(label="✅ Detective Analysis Complete", state="complete")
            
            # Step 2: Agent Pipeline
            with st.status("✍️ Newsroom Agents Working...", expanded=True) as status:
                st.write("Drafting Narrative...")
                results = run_agent_pipeline(analysis, st.session_state['history'])
                status.update(label="✅ Report Generated", state="complete")

            # Display Results
            st.divider()
            st.markdown(f"### {results['article'].splitlines()[0]}") # Mock Headline parsing
            st.info(results['article'])
            
            st.success("### 🧠 Strategic Advice")
            st.markdown(results['strategy'])
            
            # Show Memory Log (Requirement Check)
            with st.expander("View Agent Memory Logs"):
                st.json(st.session_state['history'])