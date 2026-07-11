## Import Required Library
import matplotlib.pyplot as plt

# Create Labels
# Store the names of payment methods.
payment_methods = ["Credit Card", "Debit Card", "Cash",
                   "Online Wallet", "Bank Transfer"]

### Explanation
# This list contains payment method names.
# These labels will appear on the Pie Chart.

# Create Data
# Store the number of transactions.

counts = [350, 250, 150, 180, 70]

### Explanation
# This list contains the number of transactions
# for each payment method.

# Create Colors
# Assign a different color to each pie slice.

colors = ["#4C72B0", "#DD8452", "#55A868",
          "#C44E52", "#8172B2"]

### Explanation
# Each slice of the Pie Chart will have a different color.

# Create Figure
# Set the chart size.

plt.figure(figsize=(8,8))

### Explanation
# **figure()** creates a new chart.
# **figsize=(8,8)** sets the chart width and height.

# Draw Pie Chart

plt.pie(
    counts,
    labels=payment_methods,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90
)

### Explanation
# **pie()** creates a Pie Chart.
# counts -> Pie slice sizes.
# labels -> Slice names.
# colors -> Slice colors.
# autopct="%1.1f%%" displays percentages.
# shadow=True adds a shadow effect.
# startangle=90 rotates the chart to start at 90°.

# Add Chart Title

plt.title("Payment Method Distribution")

### Explanation
# Displays the title at the top of the chart.

# Adjust Layout

plt.tight_layout()

### Explanation
# Automatically adjusts spacing.

# Save Chart

plt.savefig("payment_method_distribution.png")

### Explanation
# Saves the chart as a PNG image.

# Display Chart

plt.show()

### Explanation
# Displays the chart on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create payment method labels.
# - Create transaction data.
# - Assign colors.
# - Create a figure.
# - Draw a Pie Chart.
# - Show percentage labels.
# - Add shadow effect.
# - Rotate the chart.
# - Add title.
# - Adjust layout.
# - Save the chart.
# - Display the chart.