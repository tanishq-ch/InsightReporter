# 📰 InsightReporter: The AI Data Journalist
### Enterprise Agent Track | Google AI Agents Intensive Capstone

> **"Stop looking at dashboards. Start reading the story."**

---

## 🎯 The Problem
In the modern enterprise, **Dashboards are dead.** Executives and managers are drowning in CSVs and Tableau charts. They can see *that* revenue is down, but they have to spend hours digging into rows of data to understand *why*, and even longer to figure out *what to do about it*.

**The Gap:** There is a disconnect between **Hard Data** (SQL/Excel) and **Business Strategy** (Decision Making).

## 💡 The Solution
**InsightReporter** is an autonomous **Multi-Agent System** that acts as a 24/7 Data Journalist for your company. 

Instead of asking you to analyze charts, it proactively:
1.  **Investigates** raw data using Python tools to find anomalies.
2.  **Writes** a "Breaking News" style article explaining the context.
3.  **Advises** on strategic next steps.

It transforms passive data viewing into active strategic intelligence.

---

## ⚙️ Architecture & Implementation

InsightReporter utilizes a **Sequential Multi-Agent Architecture** powered by **Google Gemini 1.5 Flash**.

### The Agent Team
| Agent | Role | Tooling | Function |
| :--- | :--- | :--- | :--- |
| **🕵️‍♂️ Detective** | Data Analyst | `pandas`, `numpy` | Executes Python code to mathematically identify the "worst performing month" or "highest churn spike." |
| **✍️ Editor** | Journalist | `Context Injection` | Synthesizes the Detective's raw numbers into a human-readable "Morning Briefing" narrative. |
| **🧠 Strategist** | Advisor | `Reasoning Engine` | Analyzes the Editor's report to generate concrete, actionable business recommendations. |

### Technical Stack
* **LLM:** Google Gemini 1.5 Flash (via `google-generativeai`)
* **Frontend:** Streamlit (for rapid, production-grade UI)
* **Data Processing:** Pandas & Numpy
* **Visualization:** Plotly Express (Dual-Axis Charts)
* **Observability:** Custom session logging to track Agent thought processes in real-time.

---

## 🚀 Key Features (Competition Requirements)

### ✅ 1. Multi-Agent System (Sequential)
The system passes state down a chain:
`Raw CSV` → **Detective** → `Anomaly JSON` → **Editor** → `News Draft` → **Strategist** → `Final Report`.

### ✅ 2. Custom Tools
The **Detective Agent** does not hallucinate numbers. It uses a custom Python function (`analyze_worst_month`) to perform actual arithmetic on the dataset, ensuring 100% factual accuracy.

### ✅ 3. Observability & Memory
The application features a dedicated **"Agent Logs"** tab. This allows users to see the "thought traces" and JSON state of every agent, allowing users to audit the AI's decision-making process in real-time.

### ✅ 4. Robust Error Handling
The system implements **Exponential Backoff Retry Logic** to handle API rate limits (`429 Resource Exhausted`) gracefully, ensuring production-grade stability.

---

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.10+
* A Google AI Studio API Key ([Get one here](https://aistudio.google.com/))

### Step 1: Clone & Install
```bash
git clone [https://github.com/YOUR_USERNAME/InsightReporter.git](https://github.com/YOUR_USERNAME/InsightReporter.git)
cd InsightReporter
pip install -r requirements.txt

```
### Step 2: Configure API Key
Create a `.env` file in the root directory (do not upload this to GitHub):
```bash
GOOGLE_API_KEY=your_actual_api_key_here

```
### Step 3: Generate Mock Data
Create a realistic enterprise dataset (5 years of history) with one command:
```bash
python data_generator.py
```
*Output: `✅ Generated 60 months of data with 6 metrics.`*


### Step 4: Run the App
```bash
streamlit run main_app.py

```
## 📖 Usage Guide
1.  **Load Data:** The app automatically loads the `company_data.csv`. You can view the raw dataframe and charts on the left panel.
2.  **Dispatch Agents:** Click the **"🚀 Dispatch Agent Team"** button.
3.  **Watch the Process:**
    * The progress bar tracks the hand-off between Detective, Editor, and Strategist.
    * A "Breaking News" article appears on the main screen.
4.  **Check Observability:** Click the **"🛠️ Agent Memory"** tab to see the JSON logs and internal reasoning of every agent step.

---

## 📂 Project Structure
```text
InsightReporter/
│
├── .env                   # API Keys (Not uploaded to GitHub)
├── requirements.txt       # Dependencies
├── README.md              # Documentation
├── data_generator.py      # Utility to create mock Big Data
├── main_app.py            # The Frontend (Streamlit)
│
└── src/
    ├── __init__.py
    ├── tools.py           # Python Data Analysis Tools
    └── agents.py          # AI Agent Logic, Retry Logic & Observability

```
## 🏆 Innovation & Impact
While many agents act as passive chatbots, **InsightReporter** is a **Proactive Intelligence System**. It demonstrates how LLMs can bridge the gap between "Data Science" and "Executive Summary," reducing the time-to-insight from hours to seconds.
