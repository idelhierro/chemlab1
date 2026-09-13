#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt
import statistics

# Measurements of water density (g/mL)
measurements = [0.933, 0.977, 0.977, 0.982, 0.980]

# Measurement numbers
measurement_numbers = [1, 2, 3, 4, 5]

# Calculate the average density
average_density = sum(measurements) / len(measurements)

# Calculate the standard deviation
standard_deviation = statistics.stdev(measurements)

# Actual density of water at 20.1 °C (g/mL)
actual_density = 0.998

# Create the bar graph
plt.bar(
    measurement_numbers,
    measurements,
    yerr=standard_deviation,
    capsize=5,
    color="hotpink",
    label="Measured Density"
)

# Add a line for the actual density
plt.axhline(
    y=actual_density,
    linestyle="--",
    color="blue",
    label="Actual Density (0.998 g/mL)"
)

# Add a line for the average density
plt.axhline(
    y=average_density,
    linestyle="-",
    color="purple",
    label=f"Average Density ({average_density:.3f} g/mL)"
)

# Add labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("The Density of Water (20.1 °C) from a Graduate Cylinder")

# Show measurement numbers on the x-axis
plt.xticks(measurement_numbers)

# Set the y-axis range
plt.ylim(0.850, 1.05)

# Add a light grid
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Show the legend
plt.legend()

# Display the graph
plt.show()
