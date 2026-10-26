
import pandas as pd

# Load cleaned dataset
data = pd.read_csv("data/retail_sales_cleaned.csv")

# Total revenue
total_revenue = data["total_revenue"].sum()

# Total units sold
total_units = data["units_sold"].sum()

# Average order-line revenue
average_revenue = data["total_revenue"].mean()

# Best category
category_sales = data.groupby("product_category")["total_revenue"].sum()
best_category = category_sales.idxmax()

# Best region
region_sales = data.groupby("store_region")["total_revenue"].sum()
best_region = region_sales.idxmax()

# Best product by revenue
product_sales = data.groupby("product_name")["total_revenue"].sum()
best_product = product_sales.idxmax()

# Display business insights
print("===== RETAIL SALES BUSINESS INSIGHTS =====")

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Units Sold: {total_units:,.0f}")
print(f"Average Revenue per Row: ₹{average_revenue:,.2f}")

print(f"Highest Revenue Category: {best_category}")
print(f"Highest Revenue Region: {best_region}")
print(f"Highest Revenue Product: {best_product}")
