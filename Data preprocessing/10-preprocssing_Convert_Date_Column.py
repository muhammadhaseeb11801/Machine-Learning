## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")


# Check Data Type Before Conversion
# Display the data type of the Date column before conversion.
print("Before Conversion")
print(df["Date"].dtype)

### Explanation
# **dtype** shows the current data type of the Date column.
# Before conversion, the Date column is usually stored as **object (string)**.

# Convert Date Column to Datetime
# Convert the Date column into datetime format.

df["Date"] = pd.to_datetime(df["Date"])

### Explanation
# **pd.to_datetime()** converts text dates into datetime format.
# This allows us to perform date operations such as:
# - Extract Year
# - Extract Month
# - Extract Day
# - Extract Day Name
# - Calculate Date Difference

# Check Data Type After Conversion
# Display the data type after conversion.

print("\nAfter Conversion")
print(df["Date"].dtype)

### Explanation
# After conversion, the Date column becomes **datetime64[ns]**.
# This confirms that the conversion was successful.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Check the data type before conversion.
# - Convert the Date column into datetime format.
# - Verify the data type after conversion.