## Import Required Library
import matplotlib.pyplot as plt

# Create Unit Price Data
# Store the unit price values.

unit_prices = [150, 200, 175, 300, 250, 220, 180, 320, 400, 210,
               190, 260, 280, 310, 150, 170, 230, 240, 350, 290,
               160, 200, 210, 330, 270, 250, 190, 220, 380, 300,
               160, 180, 240, 260, 310, 200, 220, 290, 340, 210,
               150, 230, 250, 280, 300, 190, 210, 260, 320, 240]

### Explanation
# This list contains unit price values.
# These values are used to create the Histogram.

# Create Figure
# Set the size of the chart.
plt.figure(figsize=(10,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(10,6)** sets the width and height of the chart.

# Draw Histogram
plt.hist(
    unit_prices,
    bins=10,
    color="#DD8452",
    edgecolor="black"
)

### Explanation
# **plt.hist()** creates a Histogram.
# unit_prices -> Input data.
# bins=10 divides the data into 10 groups (intervals).
# color sets the bar color.
# edgecolor adds a black border around each bar.

# Add Chart Title
plt.title("Unit Price Histogram")

### Explanation
# Displays the title at the top of the chart.

# Add X-axis Label
plt.xlabel("Unit Price (Rs.)")

### Explanation
# Labels the horizontal (X) axis.

# Add Y-axis Label
plt.ylabel("Frequency")

### Explanation
# Labels the vertical (Y) axis.
# Frequency means how many times each price appears.

# Adjust Layout
plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so labels are not cut off.

# Save Chart
plt.savefig("unit_price_histogram.png")

### Explanation
# Saves the chart as a PNG image.

# Display Chart
plt.show()

### Explanation
# Displays the Histogram on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create unit price data.
# - Create a figure.
# - Draw a Histogram.
# - Divide data into 10 bins.
# - Add title.
# - Add X-axis label.
# - Add Y-axis label.
# - Adjust layout.
# - Save the chart.
# - Display the chart.