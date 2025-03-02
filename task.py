import matplotlib.pyplot as plt
import numpy as np

# Define the function
def F(x):
    return 100 * x / (200 - x)

# For x in [1, 199], sample densely using a linear spacing.
x_left = np.linspace(1, 199, 1000)
y_left = F(x_left)

# For x in [201, 1e9], use logarithmic spacing to capture details over many orders of magnitude.
x_right = np.logspace(np.log10(201), np.log10(1e9), 1000)
y_right = F(x_right)

plt.figure(figsize=(10, 6))

# Plot the left branch (x < 200) and right branch (x > 200) on the same axes using a log-scale for x.
plt.semilogx(x_left, y_left, label="F(x) for x < 200", color='blue')
plt.semilogx(x_right, y_right, label="F(x) for x > 200", color='orange')

# Mark the vertical asymptote at x = 200.
plt.axvline(x=200, color='red', linestyle='--', label="x = 200 (vertical asymptote)")

# Mark the horizontal asymptote at y = -100.
plt.axhline(y=-100, color='green', linestyle='--', label="y = -100 (horizontal asymptote)")

plt.xlabel("x (log scale)")
plt.ylabel("F(x)")
plt.title("Graph of F(x) = 100x / (200 - x) for x in [1, 10^9]")
plt.legend()
plt.grid(True, which="both", ls="--")

plt.show()
