# estimate value of function f(0.21) and f(0.29) applying newtons forward and backward interpolation formulae on the table 
# x= 0.20   0.22   0.24   0.26   0.28   0.30
# y= 1.6596 1.6698 1.6804 1.6912 1.7024 1.7139
#algorithm:
# 1. Define the x and y values as lists
# 2. Implement the Newton's forward and backward interpolation formulae
# 3. Use the formulae to estimate the value of the function at x=0.
# 4. Print the estimated values
# 5. Compare the estimated values with the actual value of the function at x=0.
# 6. Print the absolute error between the estimated and actual values
# 7. Repeat the process for x=0.29
# 8. Print the final answer

import math
import numpy as np
import os
import matplotlib.pyplot as plt

# Function to compute factorial
def factorial(n):
    return math.factorial(n)

# Build finite forward difference table
def forward_difference_table(y_values):
    n = len(y_values)
    diff_table = [y_values[:]]
    for level in range(1, n):
        prev = diff_table[level - 1]
        curr = [round(prev[i+1] - prev[i], 7) for i in range(n - level)]
        diff_table.append(curr)
    return diff_table

# Newton's Forward Interpolation
def newton_forward(x_values, y_values, x_to_find):
    h = round(x_values[1] - x_values[0], 2)
    u = (x_to_find - x_values[0]) / h

    table = forward_difference_table(y_values)
    result = y_values[0]
    u_term = 1

    for i in range(1, len(table)):
        u_term *= (u - (i - 1))
        term = (u_term * table[i][0]) / factorial(i)
        result += term

    return round(result, 7)

# Newton's Backward Interpolation
def newton_backward(x_values, y_values, x_to_find):
    h = round(x_values[1] - x_values[0], 2)
    n = len(x_values)
    u = (x_to_find - x_values[-1]) / h  # backward uses last point
    table = forward_difference_table(y_values)
    result = y_values[-1]
    u_term = 1

    for i in range(1, len(table)):
        index = len(table[i]) - 1  # last index for backward
        if index < 0:
            break
        u_term *= (u + (i - 1))
        term = (u_term * table[i][index]) / factorial(i)
        result += term

    return round(result, 7)

 #interpolated points across the full x range
def generate_interpolated_curve(x_vals, y_vals, method='forward', resolution=100):
    x_min, x_max = x_vals[0], x_vals[-1]
    x_interp = np.linspace(x_min, x_max, resolution)
    y_interp = []

    for x in x_interp:
        if x <= x_vals[len(x_vals)//2]:
            y = newton_forward(x_vals, y_vals, x)
        else:
            y = newton_backward(x_vals, y_vals, x)
        y_interp.append(y)

    return x_interp, y_interp

# Save results to file
def save_results(x_vals, y_vals, f1, f2, filename="results/newton-interpolation-output.txt"):
    os.makedirs("results", exist_ok=True)
    with open(filename,"wt") as f:
        f.write("x-values: " + ", ".join(map(str, x_vals)) + "\n")
        f.write("y-values: " + ", ".join(map(str, y_vals)) + "\n")
        f.write(f"f(0.21) using Forward Interpolation: {f1}\n")
        f.write(f"f(0.29) using Backward Interpolation: {f2}\n")
    print(f"\nResults saved to {filename}")


# Plot the result
def plot_interpolation(x_vals, y_vals, f1, f2, x1, x2):
    x_interp, y_interp = generate_interpolated_curve(x_vals, y_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'o-', label='Original Points')
    plt.plot(x_interp, y_interp, '-', label='Newton Interpolated Curve', color='blue')
    plt.scatter([x1], [f1], color='green', marker='s', s=80, label=f'f({x1}) ≈ {f1}')
    plt.scatter([x2], [f2], color='red', marker='s', s=80, label=f'f({x2}) ≈ {f2}')
    plt.title("Newton Forward and Backward Interpolation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    x_vals = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30]
    y_vals = [1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139]

    x1 = 0.21
    x2 = 0.29

    f1 = newton_forward(x_vals, y_vals, x1)
    f2 = newton_backward(x_vals, y_vals, x2)

    print("\n==========================")
    print(" Newton Interpolation Results")
    print("==========================")
    print(f"Estimated f({x1}) using Forward Interpolation: {f1}")
    print(f"Estimated f({x2}) using Backward Interpolation: {f2}")

    save_results(x_vals, y_vals, f1, f2)
    plot_interpolation(x_vals, y_vals, f1, f2, x1, x2)
    print("\nPlotting the interpolation results...")
    print("Plot displayed above.")
    