import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "data/CustomerData_Composite.csv"
data = pd.read_csv(file_path)

# Ensure all columns are lowercase to prevent key errors
data.columns = [col.lower().replace(" ", "_") for col in data.columns]

# Select numerical variables
numerical_vars = [
    "age",
    "number_of_dependents",
    "total_population",
    # "latitude",
    # "longitude",
    "monthly__charges",
    "avg_monthly_long_distance_charges",
    "total_charges",
    "total_refunds",
    "total_extra_data_charges",
    "total_long_distance_charges",
    "total_revenue",
    "tenure",
    "avg_monthly_gb_download",
    "number_of_referrals",
    "cltv",
]

# Verify that all variables exist in the dataset
available_vars = [var for var in numerical_vars if var in data.columns]
missing_vars = [var for var in numerical_vars if var not in data.columns]
if missing_vars:
    print(
        f"Warning: The following variables are missing from the dataset: {missing_vars}"
    )

# Compute the correlation matrix for available variables
correlation_matrix = data[available_vars].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Plot the correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Matrix Heatmap")
plt.show()

# Identify highly correlated variables (correlation > 0.8 or < -0.8)
high_corr_pairs = []
threshold = 0.8
for i in range(len(correlation_matrix.columns)):
    for j in range(i + 1, len(correlation_matrix.columns)):
        corr_value = correlation_matrix.iloc[i, j]
        if abs(corr_value) > threshold:
            high_corr_pairs.append(
                (
                    correlation_matrix.columns[i],
                    correlation_matrix.columns[j],
                    corr_value,
                )
            )

if high_corr_pairs:
    print("Highly Correlated Pairs:")
    for pair in high_corr_pairs:
        print(f"{pair[0]} and {pair[1]}: Correlation = {pair[2]:.2f}")

    # Scatter plot for the first highly correlated pair
    var_x, var_y = high_corr_pairs[0][0], high_corr_pairs[0][1]
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=var_x, y=var_y, alpha=0.6)
    plt.title(f"Scatter Plot: {var_x} vs {var_y}")
    plt.xlabel(var_x)
    plt.ylabel(var_y)
    plt.show()
else:
    print("No highly correlated pairs found.")
