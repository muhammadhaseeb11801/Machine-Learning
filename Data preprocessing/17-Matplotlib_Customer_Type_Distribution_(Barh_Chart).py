## Import Required Library
import matplotlib.pyplot as plt

# Create Y-axis Data
# Store different customer types.
customer_types = ["New", "Returning", "Loyal", "Wholesale"]

### Explanation
# This list contains different customer categories.
# These values will appear on the Y-axis
# because we are using a horizontal bar chart.

# Create X-axis Data
# Store the number of customers.
counts = [120, 200, 150, 60]

### Explanation
# This list contains the total number of customers
# in each customer category.
# These values will appear on the X-axis.

# Create Colors
# Assign different colors to each bar.
colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

### Explanation
# Each bar will have a different color,
# making the chart easier to understand.

# Create Figure
# Set the size of the chart.
plt.figure(figsize=(8, 6))

### Explanation
# figure() creates a new chart.
# figsize=(8,6) sets the width and height
# of the figure in inches.

# Draw Horizontal Bar Chart
bars = plt.barh(customer_types, counts, color=colors, height=0.5)

### Explanation
# plt.barh() creates a horizontal bar chart.
# customer_types are displayed on the Y-axis.
# counts are displayed on the X-axis.
# color=colors assigns a different color
# to each bar.
# height=0.5 controls the thickness of the bars.

# Add Chart Title
plt.title("Customer Type Distribution")

### Explanation
# Displays the title at the top of the chart.

# Add X-axis Label
plt.xlabel("Number of Customers")

### Explanation
# Labels the horizontal (X) axis.
# It represents the number of customers.

# Add Y-axis Label
plt.ylabel("Customer Type")

### Explanation
# Labels the vertical (Y) axis.
# It represents the different customer categories.

# Add Grid
plt.grid(axis="x", linestyle="-", alpha=0.7, color="black")

### Explanation
# Displays solid grid lines on the X-axis.
# linestyle="-" creates solid grid lines.
# alpha=0.7 makes the grid slightly transparent.
# color="black" sets the grid color to black.

# Adjust Layout
plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so titles and labels are not cut off.

# Save Chart
plt.savefig("customer_type_distribution.png")

### Explanation
# Saves the chart as a PNG image
# in the current project folder.

# Display Chart
plt.show()

### Explanation
# Displays the chart on the screen.

# Summary

# This program performs the following steps:
# - Import the Matplotlib library.
# - Create customer type data.
# - Create customer count data.
# - Assign different colors to each bar.
# - Create a figure.
# - Draw a horizontal bar chart.
# - Add a chart title.
# - Label the X-axis.
# - Label the Y-axis.
# - Add grid lines.
# - Adjust the layout.
# - Save the chart as a PNG image.
# - Display the chart.