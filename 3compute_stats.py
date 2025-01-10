import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset
file_path = "data/CustomerData_Composite.csv" 
data = pd.read_csv(file_path)

# List of variables to analyze
variables = [
    "age",
    "monthly__charges",
    "avg_monthly_long_distance_charges",
    "total_charges",
    "total_long_distance_charges",
    "total_revenue",
    "tenure",
    "avg_monthly_gb_download",
    "satisfaction_score",
    "cltv",
    "churn_score"
]

# Clean column names to remove leading/trailing spaces and standardize formatting
data.columns = data.columns.str.strip().str.replace(' ', '_')

# Convert columns to numeric, forcing errors to NaN for invalid entries
for col in variables:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Function to compute statistics for a variable
def compute_statistics(df, column):
    try:
        mean = df[column].mean()
        std_dev = df[column].std()
        median = df[column].median()
        mode = df[column].mode()[0] if not df[column].mode().empty else None
        quartiles = {
            "25%": df[column].quantile(0.25),
            "50%": df[column].quantile(0.50),
            "75%": df[column].quantile(0.75)
        }
        
        return {
            "mean": mean,
            "std_dev": std_dev,
            "median": median,
            "mode": mode,
            "quartiles": quartiles
        }
    except Exception as e:
        return {"error": str(e)}

# Compute statistics for each variable
statistics = {}
for col in variables:
    statistics[col] = compute_statistics(data, col)

# Display results
for col, stats in statistics.items():
    print(f"Statistics for {col}:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print("\n")
