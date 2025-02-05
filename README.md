# Customer Data Analysis & CLTV Insights

## Overview
This repository contains a data science project focused on analyzing customer data and predicting **Customer Lifetime Value (CLTV)**. The project leverages **descriptive statistics, correlation analysis, and segmentation techniques** to uncover insights from customer behavior.

## Project Structure
- **`4compute_stats.py`** – Computes **descriptive statistics** (mean, median, mode, quartiles) for key customer variables.
- **`5correlation_analysis.py`** – Performs **correlation analysis** to identify relationships between customer attributes.
- **`6average_cltv.py`** – Analyzes **CLTV trends** across age groups and gender segmentation.
- **`CustomerData_Composite.csv`** – Dataset containing customer demographic, service, and billing information.

## Features & Methodologies

### 1. Descriptive Statistics (`4compute_stats.py`)
- Computes summary statistics for customer-related variables:
  - **Age, Monthly Charges, Total Revenue, Tenure, CLTV, Churn Score**
- Identifies **data distributions and trends** within customer attributes.

### 2. Correlation Analysis (`5correlation_analysis.py`)
- Calculates **Pearson correlation coefficients** for numerical features.
- Highlights **highly correlated variable pairs** (e.g., total charges vs. total revenue).
- **Visualizes correlations** using a heatmap and scatter plots.

### 3. CLTV Segmentation (`6average_cltv.py`)
- Groups customers into **age segments (15-25, 26-35, etc.)**.
- Computes **average CLTV by gender and age group**.
- Generates **bar charts** to illustrate CLTV trends across demographics.

## Results & Insights

### Descriptive Statistics Findings
- **Average Customer Age:** ~46 years old
- **Mean Monthly Charges:** ~$64.76
- **Median CLTV:** ~$4527
- **Churn Score Distribution:** Customers with a higher churn score have lower tenure and revenue.

### Correlation Analysis Insights
- **Total Charges & Total Revenue** are **highly correlated (0.97)**, suggesting they measure similar aspects of customer spending.
- **Tenure has a strong correlation with Total Charges (0.83)**, indicating longer-term customers tend to have higher total spending.

### CLTV Segmentation Findings
- **Customers aged 36-45 have the highest average CLTV.**
- **CLTV is slightly higher for males than females in most age groups.**
- **There is variability across age segments, with older customers exhibiting slightly lower CLTV.**