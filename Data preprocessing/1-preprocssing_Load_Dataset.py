## Import Required Library
import pandas as pd  # Import the Pandas library for data manipulation.

### Explanation
# **Pandas** is a Python library used for reading, managing,
# and analyzing datasets.
# We use **pd** as the short name (alias) of Pandas.

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.

df = pd.read_csv("data.csv")

### Explanation
# **pd.read_csv()** reads the CSV file.
# The dataset is stored in a Pandas DataFrame called **df**.
# A DataFrame is a table made up of rows and columns.

# Display Dataset
# Print all rows and columns of the dataset.

print(df)

### Explanation
# **print(df)** displays the complete dataset.
# It helps verify that the file has been loaded successfully.
# If the dataset is very large, the first and last rows are shown,
# while the middle rows may be abbreviated.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Store the dataset in a DataFrame named df.
# - Display the complete dataset.
# - Verify that the dataset has been loaded successfully.