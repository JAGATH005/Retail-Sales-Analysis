
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("data/retail_sales_cleaned.csv")

# Calculate revenue for each product
product_sales = data.groupby("product_name")["total_revenue"].sum()

# Select top 10 products
top_products = product_sales.sort_values(
    ascending=False
).head(10)

# Display results
print("Top 10 Products by Revenue:")
print(top_products.round(2))

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Total Revenue (₹)")
plt.ylabel("Product Name")
plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("outputs/top_products.png", dpi=300)
plt.show()
