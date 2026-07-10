## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Display Descriptive Statistics
# Show statistical summary of all numerical columns.
print(df.describe())

### Explanation
# **describe()** returns a statistical summary of numerical columns.
# It displays important statistics such as:
# count -> Total number of values
# mean  -> Average value
# std   -> Standard deviation
# min   -> Minimum value
# 25%   -> First Quartile
# 50%   -> Median
# 75%   -> Third Quartile
# max   -> Maximum value

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Store the dataset in a DataFrame named df.
# - Display descriptive statistics.
# - Understand the numerical data.