
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("data/retail_sales_cleaned.csv")

# Convert date into datetime format
data["date"] = pd.to_datetime(data["date"])

# Group sales by month
data["year_month"] = data["date"].dt.to_period("M")
monthly_sales = data.groupby("year_month")["total_revenue"].sum()

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")

# Add chart details
plt.title("Monthly Retail Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Revenue (₹)")
plt.xticks(rotation=90)
plt.grid(True)

# Save the chart
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png", dpi=300)

# Display the chart
plt.show()

print("Monthly sales chart saved successfully!")
