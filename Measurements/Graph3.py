#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt
import statistics

# Measurements of penny density (g/cm^3)
measurements = [7.5, 8.5, 7.0, 9.1]

# Measurement numbers
measurement_numbers = [1, 2, 3, 4]

# Calculate the average density
average_density = sum(measurements) / len(measurements)

# Calculate the standard deviation
standard_deviation = statistics.stdev(measurements)

# Actual density of the penny (g/cm^3)
# Replace this value with the accepted density given by your lab.
actual_density = 8.96

# Create the bar graph
plt.bar(
    measurement_numbers,
    measurements,
    yerr=standard_deviation,
    capsize=5,
    color="hotpink",
    label="Measured Density"
)

# Add a line for the average density
plt.axhline(
    y=average_density,
    linestyle="-",
    color="purple",
    label=f"Average Density ({average_density:.3f} g/cm³)"
)

# Add labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/cm³)")
plt.title("The Density of a Penny")

# Show measurement numbers on the x-axis
plt.xticks(measurement_numbers)

# Set the y-axis range
plt.ylim(0.00, 11)

# Add a light grid
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Show the legend
plt.legend()

# Display the graph
plt.show()