## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.

df = pd.read_csv("data.csv")

# Display First 10 Rows
# Show only the first 10 records of the dataset.

print(df.head(10))

### Explanation
# **head(10)** displays the first 10 rows of the dataset.
# It helps us quickly inspect the data.
# This is useful for checking whether the dataset
# has been loaded correctly.
# By default, **head()** displays only the first 5 rows.
# Using **head(10)** displays the first 10 rows.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Store the dataset in a DataFrame named df.
# - Display the first 10 rows of the dataset.
# - Verify that the dataset has been loaded successfully.