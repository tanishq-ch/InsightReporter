# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from src.tools import get_sales_data, analyze_worst_month
# from src.agents import run_agent_pipeline
# import os

# # --- PAGE CONFIG ---
# st.set_page_config(page_title="InsightReporter", page_icon="📰", layout="wide")

# # --- HEADER ---
# st.title("📰 InsightReporter")
# st.markdown("**The AI-Powered Data Newsroom for Enterprise**")
# st.markdown("---")

# # --- SIDEBAR (Controls) ---
# with st.sidebar:
#     st.header("⚙️ Controls")
#     if st.button("🔄 Generate/Reset Mock Data"):
#         # Run the generator inline
#         from data_generator import create_dummy_data
#         create_dummy_data()
#         st.success("New data generated!")
#         st.rerun()

# # --- MAIN APP LOGIC ---

# # 1. Load Data
# df, error = get_sales_data()

# if error:
#     st.warning("⚠️ No data found. Click 'Generate Mock Data' in the sidebar.")
# else:
#     # Layout: Data on Left, Agents on Right
#     col1, col2 = st.columns([1, 1])

#     with col1:
#         st.subheader("📊 Raw Enterprise Data")
#         st.dataframe(df, use_container_width=True)
        
#         # Chart
#         st.subheader("Visual Analysis")
#         fig = px.line(df, x='Month', y=['Revenue_Millions', 'Churn_Rate'], 
#                       title="Revenue vs Churn Trends")
#         st.plotly_chart(fig, use_container_width=True)

#     with col2:
#         st.subheader("🤖 AI Agent Newsroom")
        
#         if st.button("🚀 Launch Investigation", type="primary"):
            
#             # SESSION STATE (Memory)
#             if 'history' not in st.session_state:
#                 st.session_state['history'] = []

#             # Step 1: Tool Execution
#             with st.status("🕵️‍♂️ Agent 1 (Detective): Scanning Database...", expanded=True) as status:
#                 analysis = analyze_worst_month(df)
#                 st.write(f"**Anomaly Found:** Month of {analysis['month']}")
#                 st.write(f"Churn Rate: {analysis['churn']} (Avg: {analysis['avg_churn']})")
#                 status.update(label="✅ Detective Analysis Complete", state="complete")
            
#             # Step 2: Agent Pipeline
#             with st.status("✍️ Newsroom Agents Working...", expanded=True) as status:
#                 st.write("Drafting Narrative...")
#                 results = run_agent_pipeline(analysis, st.session_state['history'])
#                 status.update(label="✅ Report Generated", state="complete")

#             # Display Results
#             st.divider()
#             st.markdown(f"### {results['article'].splitlines()[0]}") # Mock Headline parsing
#             st.info(results['article'])
            
#             st.success("### 🧠 Strategic Advice")
#             st.markdown(results['strategy'])
            
#             # Show Memory Log (Requirement Check)
#             with st.expander("View Agent Memory Logs"):
#                 st.json(st.session_state['history'])


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from src.tools import get_sales_data, analyze_worst_month
from src.agents import run_agent_pipeline

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="InsightReporter", 
    page_icon="📰", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (For that "Newsroom" Aesthetic) ---
st.markdown("""
<style>
    .big-headline {
        font-family: 'Helvetica', sans-serif;
        color: #1E3A8A;
        font-size: 32px;
        font-weight: 800;
        padding-bottom: 10px;
        border-bottom: 2px solid #1E3A8A;
        margin-bottom: 20px;
    }
    .report-text {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #3b82f6;
        font-size: 16px;
        line-height: 1.6;
        color: #1e293b;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 50px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CONTROLS ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2537/2537855.png", width=50)
    st.title("Controls")
    st.info("💡 **Track:** Enterprise Agents")
    
    st.markdown("---")
    if st.button("🔄 Generate New Mock Data"):
        # Import inside the function to avoid circular imports on startup
        from data_generator import create_dummy_data
        create_dummy_data()
        
        # Clear cache so the app reloads the new file
        st.cache_data.clear()
        st.success("✅ New Database Generated!")
        time.sleep(1)
        st.rerun()
    
    st.markdown("---")
    st.caption("InsightReporter v2.0")
    st.caption("Powered by Google Gemini 2.0")

# --- MAIN HEADER ---
st.title("📰 InsightReporter: Automated Data Journalism")
st.markdown("**Turn your spreadsheets into strategy. The AI Agent that investigates, reports, and advises.**")
st.divider()

# --- LOAD DATA ---
df, error = get_sales_data()

if error:
    st.error(f"⚠️ System Alert: {error}")
    st.warning("👈 Please click 'Generate New Mock Data' in the sidebar.")
else:
    # --- LAYOUT: 2 COLUMNS ---
    col_data, col_agent = st.columns([1.2, 1])

    # --- LEFT COLUMN: DATA VISUALIZATION ---
    with col_data:
        st.subheader("📊 Live Enterprise Data (5-Year History)")
        
        # 1. The Dataframe (Show last 12 months only for cleanliness)
        st.dataframe(df.tail(12), use_container_width=True, height=250)
        st.caption("Displaying most recent 12 months of records.")

        # 2. The Professional Dual-Axis Chart
        st.subheader("📉 Market Trends Analysis")
        
        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add Revenue (Bars)
        fig.add_trace(
            go.Bar(x=df['Month'], y=df['Revenue_Millions'], name="Revenue ($M)", marker_color='#94a3b8'),
            secondary_y=False,
        )

        # Add Churn (Line)
        fig.add_trace(
            go.Scatter(x=df['Month'], y=df['Churn_Rate'], name="Churn Rate", line=dict(color='#dc2626', width=3)),
            secondary_y=True,
        )

        # Update layout
        fig.update_layout(
            title_text="Revenue vs Churn Correlation",
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        # Set y-axes titles
        fig.update_yaxes(title_text="Revenue (Millions)", secondary_y=False)
        fig.update_yaxes(title_text="Churn Rate (0-1.0)", secondary_y=True)

        st.plotly_chart(fig, use_container_width=True)

    # --- RIGHT COLUMN: THE AGENT UI ---
    with col_agent:
        st.subheader("🤖 Agent Newsroom")
        
        # TABS: Logic vs Observability (Crucial for points!)
        tab_brief, tab_logs = st.tabs(["📝 Daily Briefing", "🛠️ Agent Memory (Observability)"])

        with tab_brief:
            st.markdown("Dispatch the AI team to analyze the latest data anomalies.")
            
            if st.button("🚀 Dispatch Agent Team", type="primary"):
                
                # 1. Initialize Session Logs for this run
                st.session_state['logs'] = []
                
                # 2. Progress Bar Animation (Visual Flair)
                progress_bar = st.progress(0, text="Initializing Agents...")
                
                # --- STEP 1: DETECTIVE AGENT ---
                time.sleep(0.5)
                progress_bar.progress(30, text="🕵️‍♂️ Detective: Scanning SQL Database for anomalies...")
                
                # Call the Tool
                analysis = analyze_worst_month(df)
                
                # --- STEP 2: EDITOR & STRATEGIST ---
                progress_bar.progress(60, text="✍️ Editor: Drafting breaking news story...")
                
                # Call the AI Pipeline
                results = run_agent_pipeline(analysis, st.session_state['logs'])
                
                progress_bar.progress(100, text="🧠 Strategist: Finalizing action plan.")
                time.sleep(0.5)
                progress_bar.empty()

                # --- STEP 3: DISPLAY RESULTS ---
                st.markdown(f'<div class="big-headline">{results["article"].splitlines()[0]}</div>', unsafe_allow_html=True)
                
                st.markdown("### 📰 The Scoop")
                st.markdown(f'<div class="report-text">{results["article"]}</div>', unsafe_allow_html=True)
                
                st.success("### 🧠 Strategic Advice")
                st.markdown(results['strategy'])

        # OBSERVABILITY TAB (The "Under the Hood" view)
        with tab_logs:
            st.info("This log tracks the sequential chain of thought between agents.")
            
            if 'logs' in st.session_state and st.session_state['logs']:
                for i, log in enumerate(st.session_state['logs']):
                    with st.expander(f"Step {i+1}: {log['agent']} ({log['action']})"):
                        st.code(log['details'], language="json" if "{" in str(log['details']) else "text")
            else:
                st.write("No agents have run yet. Click 'Dispatch' in the Briefing tab.")