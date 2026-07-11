## Import Required Library
import matplotlib.pyplot as plt

# Create Y-axis Data
# Store the names of the cities.
cities = ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Multan", "Peshawar"]

### Explanation
# This list contains city names.
# These values will appear on the Y-axis
# because we are using a horizontal bar chart.

# Create X-axis Data
# Store the revenue values.
revenue = [85000, 72000, 60000, 45000, 38000, 30000]

### Explanation
# This list contains the revenue earned
# from each city.
# These values will appear on the X-axis.

# Create Colors
# Assign different colors to each bar.
colors = ["#4C72B0", "#DD8452", "#55A868",
          "#C44E52", "#8172B2", "#937860"]

### Explanation
# Each bar will have a different color,
# making the chart more attractive
# and easier to understand.

# Create Figure
# Set the size of the chart.
plt.figure(figsize=(10, 6))

### Explanation
# figure() creates a new chart.
# figsize=(10,6) sets the width and height
# of the figure in inches.

# Draw Horizontal Bar Chart
bars = plt.barh(
    cities,
    revenue,
    color=colors,
    height=0.5
)

### Explanation
# plt.barh() creates a horizontal bar chart.
# cities are displayed on the Y-axis.
# revenue is displayed on the X-axis.
# color=colors assigns different colors
# to each bar.
# height=0.5 controls the thickness of the bars.

# Add Chart Title
plt.title("Revenue by City")

### Explanation
# Displays the chart title at the top.

# Add X-axis Label
plt.xlabel("Revenue (in Rs.)")

### Explanation
# Labels the horizontal (X) axis.
# It represents the revenue earned.

# Add Y-axis Label
plt.ylabel("City")

### Explanation
# Labels the vertical (Y) axis.
# It represents the city names.

# Add Grid
plt.grid(axis="x", linestyle="-", alpha=0.7, color="black")

### Explanation
# Displays solid grid lines on the X-axis.
# linestyle="-" creates solid grid lines.
# alpha=0.7 makes the grid slightly transparent.
# color="black" sets the grid color to black.

# Rotate Y-axis Labels
plt.yticks(rotation=45)

### Explanation
# Rotates the city names on the Y-axis
# by 45 degrees for better readability.
# This is optional because horizontal
# bar charts usually do not require
# rotated labels.

# Adjust Layout
plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so titles and labels are not cut off.

# Save Chart
plt.savefig("revenue_by_city.png")

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
# - Create city data.
# - Create revenue data.
# - Assign different colors to each bar.
# - Create a figure.
# - Draw a horizontal bar chart.
# - Add a chart title.
# - Label the X-axis.
# - Label the Y-axis.
# - Add grid lines.
# - Rotate the Y-axis labels (optional).
# - Adjust the layout.
# - Save the chart as a PNG image.
# - Display the chart.