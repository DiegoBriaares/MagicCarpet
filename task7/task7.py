import numpy as np
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
            return np.nan  # or float('inf')
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
    # (a op1 y)
    left_val = apply_op(a, y, op1)
    # (y op3 z)
    yz_val = apply_op(y, z, op3)
    # ((y op3 z) op3 x)
    right_val = apply_op(yz_val, x, op3)
    # final result: (left_val op2 right_val)
    result = apply_op(left_val, right_val, op2)
    return result

# -----------------------------------------------------------------------------
# STEP 3: Define domain for x,y,z
# -----------------------------------------------------------------------------
# Increase domain sizes if you want even more data or bigger surfaces.
x_values = np.arange(1, 21, 1)  # x in [1..20]
y_values = np.arange(1, 21, 1)  # y in [1..20]
z_values = range(1, 6)          # We'll produce separate plots for z=1..5

# Create the 2D mesh for x,y
X2d, Y2d = np.meshgrid(x_values, y_values, indexing='ij')  

# -----------------------------------------------------------------------------
# STEP 4: Generate all operator combinations
# -----------------------------------------------------------------------------
operators = ['+', '-', '*', '/']
all_combos = list(itertools.product(operators, repeat=3))

# Map operators to safe strings for filenames
safe_op_map = {
    '+': 'plus',
    '-': 'minus',
    '*': 'mul',
    '/': 'div'
}

# -----------------------------------------------------------------------------
# STEP 5: Iterate over each combination and each z-value, produce 3D surface
# -----------------------------------------------------------------------------
for ops in all_combos:
    op1, op2, op3 = ops
    # Build partial label
    combo_label = f"({op1}, {op2}, {op3})"
    
    for z_val in z_values:
        # Evaluate f(x,y,z_val) over the 2D domain
        F2d = np.zeros_like(X2d, dtype=float)
        for i_x, x_val in enumerate(x_values):
            for i_y, y_val in enumerate(y_values):
                F2d[i_x, i_y] = f_xyz(x_val, y_val, z_val, ops, a=2.0)
        
        # Plot the 3D surface
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection='3d')
        
        ax.plot_surface(X2d, Y2d, F2d, cmap='viridis', edgecolor='none')
        ax.set_title(f"f(x,y,z={z_val}) with ops={combo_label}, a=2")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel(f"f(x,y,{z_val})")
        
        # Safe filename
        op_str = f"{safe_op_map[op1]}_{safe_op_map[op2]}_{safe_op_map[op3]}"
        filename = f"f_xyz_{op_str}_z{z_val}.png"
        
        plt.tight_layout()
        plt.savefig(filename, dpi=100)
        plt.close(fig)

print("Done! A big collection of PNG files has been generated.")
