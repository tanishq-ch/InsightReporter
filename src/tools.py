import pandas as pd
import os

def get_sales_data(filepath='company_data.csv'):
    """Safe loader for the dataset."""
    if not os.path.exists(filepath):
        return None, "Data file not found. Please generate data first."
    return pd.read_csv(filepath), None

def analyze_worst_month(df):
    """
    Identifies the critical month with highest churn.
    Returns: dict with the row data and dataset context.
    """
    try:
        # Find the row with max Churn_Rate
        worst_idx = df['Churn_Rate'].idxmax()
        worst_row = df.iloc[worst_idx]
        
        # Calculate context (averages)
        avg_revenue = df['Revenue_Millions'].mean()
        avg_churn = df['Churn_Rate'].mean()
        
        return {
            "month": worst_row['Month'],
            "revenue": worst_row['Revenue_Millions'],
            "churn": worst_row['Churn_Rate'],
            "avg_revenue": round(avg_revenue, 2),
            "avg_churn": round(avg_churn, 3)
        }
    except Exception as e:
        return {"error": str(e)}