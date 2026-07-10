## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Display Last 10 Rows
# Show only the last 10 records of the dataset.
print(df.tail(10))

### Explanation
# tail(10) displays the last 10 rows of the dataset.
# It helps us inspect the ending records of the data.
# This is useful for checking whether the dataset
# contains correct values at the end.
# By default, tail() displays only the last 5 rows.
# Using tail(10) displays the last 10 rows.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Store the dataset in a DataFrame named df.
# - Display the last 10 rows of the dataset.
# - Verify the ending records of the dataset.