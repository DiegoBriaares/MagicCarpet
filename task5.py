import numpy as np
import plotly.graph_objects as go

# Use a coarser grid for performance: 50 points along each axis.
n_points = 50
x = np.linspace(1, 300, n_points)
y = np.linspace(1, 300, n_points)
z = np.linspace(1, 300, n_points)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Compute F(x,y,z) = (x*y) / (y*z - x)
with np.errstate(divide='ignore', invalid='ignore'):
    F = (X * Y) / ((Y * Z) - X)

# Identify near-singularities where the denominator is nearly zero
sing_mask = np.abs((Y * Z) - X) < 1e-9
F[sing_mask] = np.nan

# For the isosurface, choose an iso value.
# Here we take the median of the finite values as a starting point.
finite_F = F[np.isfinite(F)]
iso_value = np.median(finite_F)

# Create the isosurface plot. Adjust isomin and isomax to show the surface at the chosen iso value.
fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=F.flatten(),
    isomin=iso_value,
    isomax=iso_value,
    surface_count=1,
    colorscale='Viridis'
))

fig.update_layout(
    title=f"Isosurface of F(x,y,z) = (x*y)/(y*z - x) at iso value {iso_value:.2f}",
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z'
    )
)

fig.show()
