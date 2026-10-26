
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("data/retail_sales_cleaned.csv")

# Calculate total revenue by region
region_sales = data.groupby("store_region")["total_revenue"].sum()

# Sort highest to lowest
region_sales = region_sales.sort_values(ascending=False)

# Display results
print("Sales by Store Region:")
print(region_sales.round(2))

# Find highest revenue region
print("\nHighest Revenue Region:")
print(region_sales.idxmax())
print("Revenue:", round(region_sales.max(), 2))

# Create bar chart
plt.figure(figsize=(10, 6))
region_sales.plot(kind="bar")

plt.title("Sales by Store Region")
plt.xlabel("Store Region")
plt.ylabel("Total Revenue (₹)")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("outputs/region_sales.png", dpi=300)
plt.show()
