## Import Required Library
import matplotlib.pyplot as plt  # Import Matplotlib library for creating graphs.

### Explanation
# **Matplotlib** is a Python library used for data visualization.
# **pyplot** provides functions to create charts and graphs.
# **plt** is the short name (alias) of matplotlib.pyplot.

# Create X-axis Data
# Store the names of the months.

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

### Explanation
# This list contains the names of all 12 months.
# These values will appear on the X-axis.

# Create Y-axis Data
# Store the monthly revenue values.

revenue = [12000, 15000, 13500, 17000, 16000, 18500,
           20000, 19500, 21000, 22500, 24000, 26000]

### Explanation
# This list contains the monthly revenue values.
# These values will appear on the Y-axis.

# Create Figure
# Set the size of the chart.

plt.figure(figsize=(10,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(10,6)** sets the chart width to 10 inches
# and height to 6 inches.

# Draw Line Chart

plt.plot(months, revenue,
         marker='o',
         color='blue',
         linewidth=2)

### Explanation
# **plot()** creates a line chart.
# months -> X-axis values
# revenue -> Y-axis values
# marker='o' displays a circle on each data point.
# color='blue' makes the line blue.
# linewidth=2 sets the thickness of the line.

# Add Chart Title

plt.title("Monthly Revenue")

### Explanation
# Displays the title at the top of the chart.

# Add X-axis Label

plt.xlabel("Month")

### Explanation
# Labels the horizontal (X) axis.

# Add Y-axis Label

plt.ylabel("Revenue (in Rs.)")

### Explanation
# Labels the vertical (Y) axis.

# Adjust Layout

plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so that labels are not cut off.

# Save Chart

plt.savefig("monthly_revenue_chart.png")

### Explanation
# Saves the chart as a PNG image.

# Display Chart

plt.show()

### Explanation
# Displays the chart on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create Month data.
# - Create Revenue data.
# - Create a figure.
# - Draw a line chart.
# - Add title.
# - Add X-axis label.
# - Add Y-axis label.
# - Adjust layout.
# - Save the chart.
# - Display the chart.