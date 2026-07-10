## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Display All Column Names
# Show the names of all columns in the dataset.
print(df.columns)

### Explanation
# **columns** returns the names of all columns.
# It helps us understand the structure of the dataset.
# The output is an Index object containing all column names.

# Example Output:
# Index(['Invoice ID', 'Branch', 'City', 'Customer type',
#        'Gender', 'Product line', 'Unit price', 'Quantity',
#        'Tax 5%', 'Total', 'Date', 'Time', 'Payment',
#        'cogs', 'gross margin percentage',
#        'gross income', 'Rating'],
#       dtype='object')

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Store the dataset in a DataFrame named df.
# - Display the names of all columns.
# - Understand the structure of the dataset.