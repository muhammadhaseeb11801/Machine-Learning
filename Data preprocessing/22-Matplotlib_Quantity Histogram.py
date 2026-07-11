## Import Required Library
import matplotlib.pyplot as plt 

# Create Quantity Data
# Store the quantity values.

quantities = [1, 2, 2, 3, 1, 4, 5, 3, 2, 1, 6, 7, 2, 3, 4,
              5, 1, 2, 3, 3, 4, 8, 2, 1, 5, 6, 3, 2, 4, 9,
              1, 2, 3, 4, 5, 6, 2, 3, 1, 7, 8, 2, 3, 4, 5,
              1, 2, 3, 6, 2]

### Explanation
# This list contains quantity values.
# These values are used to create the histogram.

# Create Figure
# Set the size of the chart.

plt.figure(figsize=(10,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(10,6)** sets the width and height of the chart.

# Draw Histogram

plt.hist(
    quantities,
    bins=10,
    color="#4C72B0",
    edgecolor="black"
)

### Explanation
# **hist()** creates a Histogram.
# quantities -> Input data.
# bins=10 divides the data into 10 groups (intervals).
# color sets the bar color.
# edgecolor adds a black border around each bar.

# Add Chart Title

plt.title("Quantity Histogram")

### Explanation
# Displays the title at the top of the chart.

# Add X-axis Label

plt.xlabel("Quantity")

### Explanation
# Labels the horizontal (X) axis.

# Add Y-axis Label

plt.ylabel("Frequency")

### Explanation
# Labels the vertical (Y) axis.
# Frequency means how many times each quantity appears.

# Adjust Layout

plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so labels are not cut off.

# Save Chart

plt.savefig("quantity_histogram.png")

### Explanation
# Saves the chart as a PNG image.

# Display Chart

plt.show()

### Explanation
# Displays the Histogram on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create quantity data.
# - Create a figure.
# - Draw a Histogram.
# - Divide data into 10 bins.
# - Add title.
# - Add X-axis label.
# - Add Y-axis label.
# - Adjust layout.
# - Save the chart.
# - Display the chart.