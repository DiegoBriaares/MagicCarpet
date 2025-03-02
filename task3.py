import matplotlib.pyplot as plt
import numpy as np

# Define the function F(x)
def F(x):
    return 100 * x / (200 - x)

# Generate x-values:
# For x < 200 (function is defined and positive)
x_left = np.linspace(1, 199, 1000)
y_left = F(x_left)

# For x > 200 (function becomes negative)
x_right = np.linspace(201, 300, 1000)
y_right = F(x_right)

# Identify and highlight the points where y is between 1 and 100.
# This occurs in the left branch.
mask = (y_left >= 1) & (y_left <= 100)
x_highlight = x_left[mask]
y_highlight = y_left[mask]

plt.figure(figsize=(10, 6))

# Plot the left branch (x < 200)
plt.plot(x_left, y_left, label="F(x) for x < 200", color='blue')
# Plot the right branch (x > 200)
plt.plot(x_right, y_right, label="F(x) for x > 200", color='orange')
# Highlight the points where y is between 1 and 100
plt.scatter(x_highlight, y_highlight, s=50, color='red', label="Points with 1 ≤ F(x) ≤ 100", zorder=5)

# Draw a vertical line at the vertical asymptote x = 200
plt.axvline(x=200, color='red', linestyle='--', label="x = 200 (vertical asymptote)")

plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Graph of F(x) = 100x/(200-x) for x in [1,300] with y in [1,100] Highlighted")
plt.legend()
plt.grid(True)

plt.show()
