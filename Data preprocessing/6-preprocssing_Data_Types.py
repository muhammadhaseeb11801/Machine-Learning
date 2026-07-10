## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Display Data Types
# Show the data type of every column in the dataset.
print(df.dtypes)

### Explanation
# **dtypes** displays the data type of each column.
# It helps us understand what kind of data is stored in every column.
# Common data types include:
# object  -> Text (String)
# int64   -> Integer numbers
# float64 -> Decimal numbers
# bool    -> True or False
# datetime64 -> Date and Time

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Store the dataset in a DataFrame named df.
# - Display the data type of every column.
# - Understand the structure of the dataset.