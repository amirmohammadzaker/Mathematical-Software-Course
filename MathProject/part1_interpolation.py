import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator, CubicSpline
from sympy import symbols, expand

# 1. Define the data points given in the project prompt
x_data = np.array([1, 2, 3, 4, 5, 6])
y_data = np.array([1, 3, 5, 8, 5, 2])

print("--- Part 1: Lagrange Interpolation ---")
# 2. Perform Lagrange interpolation using BarycentricInterpolator
lagrange_interpolator = BarycentricInterpolator(x_data, y_data)

# Extract the exact mathematical formula using sympy for clear display
x_sym = symbols('x')
lagrange_expr = 0
for i in range(len(x_data)):
    # Construct Lagrange basis polynomials
    p = 1
    for j in range(len(x_data)):
        if i != j:
            p *= (x_sym - x_data[j]) / (x_data[i] - x_data[j])
    lagrange_expr += y_data[i] * p

lagrange_simplified = expand(lagrange_expr)
print("Exact formula for Lagrange interpolating polynomial:")
print(f"L(x) = {lagrange_simplified}\n")

print("--- Part 2: Spline Interpolation ---")
# 3. Perform Cubic Spline interpolation (Natural type)
# bc_type='natural' enforces the second derivative to be zero at the boundaries
cs = CubicSpline(x_data, y_data, bc_type='natural')

print("Exact piecewise formulas for the Cubic Spline (per interval):")
for i in range(len(x_data) - 1):
    # Spline coefficients for the i-th interval
    # Formula: d(x - x_i)^3 + c(x - x_i)^2 + b(x - x_i) + a
    coeffs = cs.c[:, i]
    d, c, b, a = coeffs[0], coeffs[1], coeffs[2], coeffs[3]
    print(f"Interval [{x_data[i]}, {x_data[i+1]}]:")
    print(f"  S_{i}(x) = {a} + {b:.4f}(x - {x_data[i]}) + {c:.4f}(x - {x_data[i]})^2 + {d:.4f}(x - {x_data[i]})^3")

# 4. Plotting the results for the final report
x_plot = np.linspace(1, 6, 500)
y_lagrange_plot = lagrange_interpolator(x_plot)
y_spline_plot = cs(x_plot)

plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='red', zorder=5, label='Original Data Points')
plt.plot(x_plot, y_lagrange_plot, label='Lagrange Interpolation', linestyle='--', color='blue')
plt.plot(x_plot, y_spline_plot, label='Natural Cubic Spline', linestyle='-', color='green')

plt.title('Comparison of Lagrange and Cubic Spline Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Save the plot image to be used in the report document
plt.savefig('interpolation_plot.png', dpi=300)
plt.show()