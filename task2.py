import matplotlib.pyplot as plt
import numpy as np

# Define the function
def F(x):
    return 100 * x / (200 - x)

# Create x values for the two segments:
# For x in [1, 199] (left of the asymptote)
x_left = np.arange(1, 200)
# For x in [201, 300] (right of the asymptote)
x_right = np.arange(201, 301)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the segment for x < 200
plt.plot(x_left, F(x_left), 'b-o', markersize=4, label="F(x) for x < 200")

# Plot the segment for x > 200
plt.plot(x_right, F(x_right), 'g-o', markersize=4, label="F(x) for x > 200")

# Draw a vertical line at the asymptote x = 200
plt.axvline(x=200, color='red', linestyle='--', label="x = 200 (vertical asymptote)")

# Labeling the axes and the plot
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Graph of F(x) = 100x / (200 - x) for x in [1, 300]")
plt.legend()
plt.grid(True)

plt.show()
