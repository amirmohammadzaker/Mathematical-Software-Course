import numpy as np
from scipy.integrate import trapezoid, simpson, quad

# 1. Define the target function f(x) = e^(x^2)
def f(x):
    return np.exp(x**2)

# Define the integration intervals (from 0 to 1)
a = 0
b = 1

# Number of points for Trapezoidal and Simpson's methods
# Using 101 points (100 intervals) gives high precision
num_points = 101
x_intervals = np.linspace(a, b, num_points)
y_values = f(x_intervals)

print("--- Part 3 (a): Trapezoidal and Simpson's Methods ---")

# 2. Calculate using the Trapezoidal Rule
# In newer versions of SciPy, integration uses 'trapezoid' instead of 'trapz'
integral_trapezoidal = trapezoid(y_values, x_intervals)
print(f"Trapezoidal Rule Result: {integral_trapezoidal:.8f}")

# 3. Calculate using Simpson's Rule
integral_simpson = simpson(y_values, x_intervals)
print(f"Simpson's Rule Result:    {integral_simpson:.8f}\n")


print("--- Part 3 (b): Gaussian Quadrature Method ---")

# 4. Calculate using Gaussian Quadrature (scipy.integrate.quad uses Clenshaw-Curtis/Gauss-Kronrod)
# quad returns a tuple: (integral_value, absolute_error_estimate)
integral_gaussian, abs_error = quad(f, a, b)
print(f"Gaussian Quadrature Result: {integral_gaussian:.8f}")
print(f"Estimated Absolute Error:    {abs_error:.2e}\n")


print("--- Summary & Comparison ---")
print(f"Difference (Gaussian vs Simpson):     {abs(integral_gaussian - integral_simpson):.2e}")
print(f"Difference (Gaussian vs Trapezoidal): {abs(integral_gaussian - integral_trapezoidal):.2e}")