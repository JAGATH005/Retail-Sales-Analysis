
import pandas as pd

# Load the CSV file
data = pd.read_csv("data/retail-daily-sales.csv")

# Display the first 5 rows
print(data.head())

# Check dataset size
print("\nDataset Shape:")
print(data.shape)

# Check column names
print("\nColumn Names:")
print(data.columns)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())


# Show rows that contain missing values
missing_rows = data[data.isnull().any(axis=1)]

print("\nRows with Missing Values:")
print(missing_rows.to_string())

print("\nTotal Rows with Missing Values:")
print(data.isnull().any(axis=1).sum())


# Remove rows containing missing values
data = data.dropna()

print("\nDataset Shape After Cleaning:")
print(data.shape)

print("\nMissing Values After Cleaning:")
print(data.isnull().sum())


# Convert date column to datetime
data["date"] = pd.to_datetime(data["date"])

print("\nDate Data Type:")
print(data["date"].dtype)

print("\nDate Range:")
print("Start Date:", data["date"].min())
print("End Date:", data["date"].max())


# Check numerical columns
print("\nNumerical Summary:")
print(data[[
    "units_sold",
    "unit_price",
    "total_revenue",
    "discount_pct"
]].describe())

# Check for zero or negative values
print("\nUnits sold <= 0:", (data["units_sold"] <= 0).sum())
print("Unit price <= 0:", (data["unit_price"] <= 0).sum())
print("Revenue < 0:", (data["total_revenue"] < 0).sum())

# Check revenue calculation
data["calculated_revenue"] = (
    data["units_sold"] * data["unit_price"]
)

print("\nFirst 5 Revenue Comparisons:")
print(data[[
    "units_sold",
    "unit_price",
    "total_revenue",
    "calculated_revenue"
]].head())



# Calculate revenue after discount FIRST
data["revenue_after_discount"] = (
    data["units_sold"]
    * data["unit_price"]
    * (1 - data["discount_pct"])
)

# Now display the results
print("\nRevenue Validation:")

print(
    data[
        [
            "total_revenue",
            "calculated_revenue",
            "discount_pct",
            "revenue_after_discount"
        ]
    ].head()
)

# Compare actual revenue with calculated revenue
data["revenue_difference"] = (
    data["total_revenue"] - data["revenue_after_discount"]
)

print("\nRevenue Difference:")
print(data["revenue_difference"].head())


# Save the cleaned dataset
data.to_csv(
    "data/retail_sales_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("Final dataset shape:", data.shape)
