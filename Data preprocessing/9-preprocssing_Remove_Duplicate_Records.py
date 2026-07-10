## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Check Duplicate Rows
# Count the total number of duplicate rows.
print("Duplicate Rows Before Removing")
print(df.duplicated().sum())

### Explanation
# **duplicated()** checks whether a row is duplicated.
# It returns True for duplicate rows and False for unique rows.
# **sum()** counts the total number of duplicate rows.

# Remove Duplicate Rows
# Remove all duplicate records from the dataset.

df = df.drop_duplicates()

### Explanation
# **drop_duplicates()** removes all duplicate rows.
# The cleaned dataset is stored back into **df**.

# Check Again
# Verify that all duplicate rows have been removed.

print("\nDuplicate Rows After Removing")
print(df.duplicated().sum())

### Explanation
# This checks the dataset again.
# If the output is **0**, all duplicate rows have been removed successfully.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Count duplicate rows.
# - Remove duplicate rows.
# - Verify that no duplicate rows remain.