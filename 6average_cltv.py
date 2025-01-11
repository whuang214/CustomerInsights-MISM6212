import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
    "churn_score",
]

# Clean column names to remove leading/trailing spaces and standardize formatting
data.columns = data.columns.str.strip().str.replace(" ", "_")

# Convert columns to numeric, forcing errors to NaN for invalid entries
for col in variables:
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Group age into bins of size 10
data["age_group"] = pd.cut(
    data["age"],
    bins=range(15, 105, 10),
    right=False,
    labels=["15-25", "26-35", "36-45", "46-55", "56-65", "66-75", "76-85", "86-95"],
)

# Compute the average of cltv by gender and age group
pivot_table = data.pivot_table(
    values="cltv", index="age_group", columns="gender", aggfunc="mean"
)

# Display the pivot table
print("Average CLTV by Gender and Age Group:")
print(pivot_table)

# Optional: Plot the pivot table
pivot_table.plot(kind="bar", figsize=(12, 6))
plt.title("Average CLTV by Gender and Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average CLTV")
plt.xticks(rotation=45)
plt.legend(title="Gender")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
