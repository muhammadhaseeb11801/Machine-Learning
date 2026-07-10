## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Check Missing Values
# Display the number of missing values in each column.
print("Missing Values Before Handling")
print(df.isnull().sum())

### Explanation
# **isnull()** checks whether a value is missing (NaN).
# **sum()** counts the total missing values in each column.

# Handle Missing Values

# Numeric Columns
# Replace missing values with the average (mean).

df["Unit price"] = df["Unit price"].fillna(df["Unit price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

### Explanation
# **fillna()** replaces missing values.
# **mean()** calculates the average value.
# Missing numeric values are replaced with the column average.

# Text Columns
# Replace missing values with the most frequent value (mode).

df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Payment"] = df["Payment"].fillna(df["Payment"].mode()[0])

### Explanation
# **mode()** returns the most frequently occurring value.
# **mode()[0]** selects the first most frequent value.
# Missing text values are replaced with the most common value.

# Check Missing Values Again
# Verify that all missing values have been handled.

print("\nMissing Values After Handling")
print(df.isnull().sum())

### Explanation
# This displays the number of missing values after cleaning.
# If every column shows **0**, then all missing values have been handled successfully.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Check missing values.
# - Fill missing numeric values with the mean.
# - Fill missing text values with the mode.
# - Verify that no missing values remain.