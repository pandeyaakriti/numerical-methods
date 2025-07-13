# estimate y(2) from following table using Lagrange's interpolation formula
# x= 0  1   3   4   5
# y= 0  1  81  256  625
#algorithm:
# 1. Define the x and y values as lists
# 2. Implement the Lagrange interpolation formula
# 3. Calculate the estimated value at x = 2 using the formula


import math
import numpy as np
import os
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x_to_find):
    n = len(x_values)
    result = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x_to_find - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Save results to file
def save_results(x_values, y_values, estimated_value, filename="results/lagrange-output.txt"):
    os.makedirs("results", exist_ok=True)
    with open(filename, "w") as f:
        f.write("x-values: " + ", ".join(map(str, x_values)) + "\n")
        f.write("y-values: " + ", ".join(map(str, y_values)) + "\n")
        f.write(f"Estimated value at x = {x_values[2]} is y approx {estimated_value:.4f}\n")
    print(f"\nResults saved to {filename}")

# Plot the interpolation
def plot_interpolation(x_values, y_values, estimated_value, x1, x2):
    x_range = np.linspace(min(x_values), max(x_values), 100)
    y_range = [lagrange_interpolation(x_values, y_values, x) for x in x_range]

    plt.plot(x_values, y_values, 'ro', label='Data Points')
    plt.plot(x_range, y_range, label='Lagrange Interpolation', color='pink')
    plt.scatter([x1], [estimated_value], color='green', label=f'Estimated at x={x1}')
    
    plt.title("Lagrange Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Plotting the interpolation results...")
    print("Plot displayed above.")


if __name__ == "__main__":
    x_vals = [0, 1, 3, 4, 5]
    y_vals = [0, 1, 81, 256, 625]
    x_find = 2

    y_estimated = lagrange_interpolation(x_vals, y_vals, x_find)
    print(f"Estimated value at x = {x_find} is y ≈ {y_estimated:.4f}")
    plt.plot(x_vals, y_vals, 'ro', label='Data Points')
    x_range = np.linspace(min(x_vals), max(x_vals), 100)
    y_range = [lagrange_interpolation(x_vals, y_vals, x) for x in x_range]
    plt.plot(x_range, y_range, label='Lagrange Interpolation', color='blue')
plt.legend()
plt.title("Lagrange Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
print("Plotting the interpolation results...")
print("Plot displayed above.")

save_results(x_vals, y_vals, y_estimated)
plot_interpolation(x_vals, y_vals, y_estimated, x_find, y_estimated)
print("\nResults saved to file and plot displayed.")    
