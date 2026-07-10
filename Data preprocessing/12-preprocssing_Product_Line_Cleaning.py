## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Convert Product Line to Upper Case
# Convert all product names into uppercase letters.
df["Product line"] = df["Product line"].str.upper()

### Explanation
# **str.upper()** converts every letter into uppercase.
# Example:
# Health and beauty  →  HEALTH AND BEAUTY
# Electronic accessories → ELECTRONIC ACCESSORIES

# Remove Extra Spaces
# Remove unwanted spaces from the beginning and end of each value.

df["Product line"] = df["Product line"].str.strip()

### Explanation
# **str.strip()** removes extra spaces from both sides of the text.
# Example:
# "  FOOD AND BEVERAGES  "
# becomes
# "FOOD AND BEVERAGES"

# Display First 10 Rows
# Display the first 10 cleaned Product Line values.

print(df["Product line"].head(10))

### Explanation
# **head(10)** displays the first 10 values
# after cleaning the Product line column.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the dataset.
# - Convert Product Line values to uppercase.
# - Remove extra spaces.
# - Display the first 10 cleaned values.