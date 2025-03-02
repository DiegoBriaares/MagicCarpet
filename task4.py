import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create arrays for x and y (from 1 to 300)
x = np.arange(1, 301)
y = np.arange(1, 301)
X, Y = np.meshgrid(x, y)

# Compute the function, handling division by zero
with np.errstate(divide='ignore', invalid='ignore'):
    Z = (Y * X) / ((2 * Y) - X)
# Mask values where the denominator is (nearly) zero
denom = (2 * Y) - X
Z[np.abs(denom) < 1e-9] = np.nan

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

ax.set_title('Surface Plot of F(x, y) = y*x / (2*y - x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('F(x, y)')

fig.colorbar(surface, shrink=0.5, aspect=5)
plt.show()
