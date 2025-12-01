import pandas as pd
import numpy as np
import datetime

def create_dummy_data():
    print("🔄 Generating Enterprise-Grade Dataset...")
    
    # 1. Setup Date Range (5 Years of Monthly Data)
    # CHANGED: Used 'M' instead of 'ME' for compatibility
    dates = pd.date_range(start='2020-01-01', periods=60, freq='M')
    
    # 2. Create Base Trends (Steady Growth)
    n = len(dates)
    trend = np.linspace(10, 20, n)  # Revenue grows from 10M to 20M
    noise = np.random.normal(0, 0.5, n) # Random fluctuation
    
    revenue = trend + noise
    
    # 3. Generate Correlated Metrics
    active_users = (revenue * 500) + np.random.randint(-200, 200, n)
    marketing_spend = (revenue * 0.2) + np.random.normal(0, 0.1, n)
    churn_rate = np.random.uniform(0.01, 0.03, n)
    tickets = (active_users * 0.05) + np.random.randint(-50, 50, n)

    # 4. INJECT THE "CRISIS"
    crisis_idx = -2 
    
    revenue[crisis_idx] = revenue[crisis_idx] * 0.6
    churn_rate[crisis_idx] = 0.18
    tickets[crisis_idx] = tickets[crisis_idx] * 3
    
    # 5. Build DataFrame
    df = pd.DataFrame({
        'Month': dates.strftime('%Y-%m-%d'),
        'Revenue_Millions': np.round(revenue, 2),
        'Active_Users': active_users.astype(int),
        'Marketing_Spend_M': np.round(marketing_spend, 2),
        'Support_Tickets': tickets.astype(int),
        'Churn_Rate': np.round(churn_rate, 3)
    })
    
    # 6. Save
    df.to_csv('company_data.csv', index=False)
    print(f"✅ Generated {n} months of data with 6 metrics.")
    print("✅ Injected anomaly at row index:", crisis_idx)

if __name__ == "__main__":
    create_dummy_data()