import numpy as np
import itertools
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# If you prefer interactive windows on some environments, you can set:
# matplotlib.use("TkAgg")  # or "Qt5Agg"

# -----------------------------------------------------------------------------
# STEP 1: Define the operations
# -----------------------------------------------------------------------------
def apply_op(a, b, op):
    """Apply the operation 'op' to (a, b)."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        # Handle potential division by zero
        if abs(b) < 1e-12:
            return np.nan  # or float('inf') if you prefer
        else:
            return a / b

# -----------------------------------------------------------------------------
# STEP 2: Define the function f for a given triple of operators
# -----------------------------------------------------------------------------
def f_xyz(x, y, z, ops, a=2.0):
    """
    f(x,y,z) = (a ops[0] y) ops[1] ( (y ops[2] z) ops[2] x ).
    ops is a 3-tuple like ('+', '-', '/').
    a is a fixed constant, e.g. 2.0.
    """
    op1, op2, op3 = ops
    left_val = apply_op(a, y, op1)        # (a op1 y)
    yz_val   = apply_op(y, z, op3)        # (y op3 z)
    right_val = apply_op(yz_val, x, op3)  # ((y op3 z) op3 x)
    result = apply_op(left_val, right_val, op2)  # (left_val op2 right_val)
    return result

# -----------------------------------------------------------------------------
# STEP 3: Generate the domain for x,y (z=5 is fixed below)
# -----------------------------------------------------------------------------
xs = np.arange(1, 11, 1)  # [1..10]
ys = np.arange(1, 11, 1)
# We'll pick z=5 in each plot, but you can loop different z if you wish.

X2d, Y2d = np.meshgrid(xs, ys, indexing='ij')  # shape => (len(xs), len(ys))

# -----------------------------------------------------------------------------
# STEP 4: Enumerate all operator combinations
# -----------------------------------------------------------------------------
operators = ['+', '-', '*', '/']
all_combos = list(itertools.product(operators, repeat=3))

# We'll map the operator symbols to safe filenames
safe_op_map = {
    '+': 'plus',
    '-': 'minus',
    '*': 'mul',
    '/': 'div'
}

# -----------------------------------------------------------------------------
# STEP 5: Loop over each combination, compute f, and plot a 3D surface (x,y,f)
# -----------------------------------------------------------------------------
for (i, ops) in enumerate(all_combos, start=1):
    op1, op2, op3 = ops
    label = f"({op1}, {op2}, {op3})"
    
    # Evaluate f(x,y, z=5) over our domain
    z_fixed_value = 5
    F2d = np.zeros_like(X2d, dtype=float)
    
    for ix, x_val in enumerate(xs):
        for iy, y_val in enumerate(ys):
            F2d[ix, iy] = f_xyz(x_val, y_val, z_fixed_value, ops, a=2.0)
    
    # -----------------------------------------------------------------------------
    # Plot a 3D surface
    # -----------------------------------------------------------------------------
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')
    
    # We can plot with plot_surface. The dimension of X2d, Y2d, F2d is (10,10).
    ax.plot_surface(X2d, Y2d, F2d, cmap='viridis', edgecolor='none')
    
    ax.set_title(f"f(x,y,z=5) with ops={label}, a=2")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x,y,5)")
    
    # Build a safe filename
    op_str = f"{safe_op_map[op1]}_{safe_op_map[op2]}_{safe_op_map[op3]}"
    filename = f"f_xyz_{op_str}.png"
    
    plt.tight_layout()
    plt.savefig(filename, dpi=100)
    plt.close(fig)

print("Done! Generated 64 PNG files (one for each triple of operators).")
