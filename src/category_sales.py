
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned dataset
data = pd.read_csv("data/retail_sales_cleaned.csv")

# 2. Calculate revenue for each category
category_sales = data.groupby("product_category")["total_revenue"].sum()

# 3. Sort from highest to lowest sales
category_sales = category_sales.sort_values(ascending=False)

# 4. Display results
print("Sales by Product Category:")
print(category_sales.round(2))

# 5. Find the best-selling category by revenue
print("\nHighest Revenue Category:")
print(category_sales.idxmax())
print("Revenue:", round(category_sales.max(), 2))

# 6. Create bar chart
plt.figure(figsize=(10, 6))
category_sales.plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue (₹)")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("outputs/category_sales.png", dpi=300)
plt.show()
