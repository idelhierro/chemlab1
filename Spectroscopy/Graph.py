#This code produces the Beer graph for the spectroscopy lab
import numpy as np
import matplotlib.pyplot as plt

# Experimental data
concentration = np.array([2, 4, 6, 8, 10, 15])
absorbance = np.array([0.060, 0.120, 0.189,
                       0.247, 0.311, 0.454])

# Linear regression
slope, intercept = np.polyfit(concentration, absorbance, 1)

# Calculate R-squared
predicted = slope * concentration + intercept
r_squared = 1 - np.sum((absorbance - predicted)**2) / \
            np.sum((absorbance - np.mean(absorbance))**2)

# Plot data and fitted line
plt.scatter(concentration, absorbance, label="Experimental Data")

x = np.linspace(0, 16, 200)
plt.plot(x, slope*x + intercept, label="Linear Regression")

# Labels and title
plt.title("Absorbance vs. Concentration (422.7 nm)")
plt.xlabel("Concentration (ppm)")
plt.ylabel("Absorbance")

# Display equation and R-squared
equation = f"y = {slope:.5f}x + {intercept:.5f}\nR² = {r_squared:.5f}"
plt.text(0.7, 0.43, equation)

plt.legend()
plt.grid(True)
plt.show()

print(equation)