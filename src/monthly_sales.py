
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("data/retail_sales_cleaned.csv")

# Convert date column
data["date"] = pd.to_datetime(data["date"])

# Extract year and month
data["year_month"] = data["date"].dt.to_period("M")

# Calculate monthly revenue
monthly_sales = data.groupby("year_month")["total_revenue"].sum()

print("Monthly Sales:")
print(monthly_sales)

# Find highest sales month
print("\nHighest Sales Month:")
print(monthly_sales.idxmax(), round(monthly_sales.max(), 2))

# Find lowest sales month
print("\nLowest Sales Month:")
print(monthly_sales.idxmin(), round(monthly_sales.min(), 2))
