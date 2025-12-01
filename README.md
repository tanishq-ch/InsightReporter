# 📰 InsightReporter: The AI Data Journalist
### Enterprise Agent Track | Google AI Agents Intensive Capstone

> **"Stop looking at dashboards. Start reading the story."**

---

## 🎯 The Problem
In the modern enterprise, **Dashboards are dead.** Executives and managers are drowning in CSVs and Tableau charts. They can see *that* revenue is down, but they have to spend hours digging into rows of data to understand *why*, and even longer to figure out *what to do about it*.

**The Gap:** There is a disconnect between **Hard Data** (SQL/Excel) and **Business Strategy** (Decision Making).

## 💡 The Solution
**InsightReporter** is an autonomous **Multi-Agent System** that acts as a 24/7 Data Journalist for your company. 

Instead of asking you to analyze charts, it:
1.  **Investigates** raw data using Python tools to find anomalies.
2.  **Writes** a "Breaking News" style article explaining the context.
3.  **Advises** on strategic next steps.

It transforms passive data viewing into active strategic intelligence.

---

## ⚙️ Architecture & Implementation

InsightReporter utilizes a **Sequential Multi-Agent Architecture** powered by **Google Gemini 2.0 Flash**.

### The Agent Team
| Agent | Role | Tooling | Function |
| :--- | :--- | :--- | :--- |
| **🕵️‍♂️ Detective** | Data Analyst | `pandas`, `numpy` | Executes Python code to mathematically identify the "worst performing month" or "highest churn spike." |
| **✍️ Editor** | Journalist | `Context Injection` | Synthesizes the Detective's raw numbers into a human-readable "Morning Briefing" narrative. |
| **🧠 Strategist** | Advisor | `Reasoning Engine` | Analyzes the Editor's report to generate concrete, actionable business recommendations. |

### Technical Stack
* **LLM:** Google Gemini 2.0 Flash (via `google-genai`)
* **Frontend:** Streamlit (for rapid, production-grade UI)
* **Data Processing:** Pandas
* **Visualization:** Plotly Express
* **Observability:** Custom session logging to track Agent thought processes in real-time.

---

## 🚀 Key Features (Competition Requirements)

### ✅ 1. Multi-Agent System (Sequential)
The system passes state down a chain:
`Raw CSV` → **Detective** → `Anomaly JSON` → **Editor** → `News Draft` → **Strategist** → `Final Report`.

### ✅ 2. Custom Tools
The **Detective Agent** does not hallucinate numbers. It uses a custom Python function (`analyze_worst_month`) to perform actual arithmetic on the dataset, ensuring 100% factual accuracy.

### ✅ 3. Observability & Memory
The application includes a dedicated **"Agent Logs"** tab. This allows users to see the "thought traces" of the agents in real-time, satisfying the requirement for observability into the AI's decision-making process.

---

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.8+
* A Google AI Studio API Key

### Step 1: Clone & Install
```bash
git clone [https://github.com/YOUR_USERNAME/InsightReporter.git](https://github.com/YOUR_USERNAME/InsightReporter.git)
cd InsightReporter
pip install -r requirements.txt