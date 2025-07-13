#approximate root if e^x= 4x by taking x0= 1.0 using newton's method
#algorithm:
# 1. Define the function f(x) = e^x - 4x and its derivative f'(x) = e^x - 4
# 2. Start with an initial guess x0=1
# 3. Calculate f(x0) and f'(x0)
# 4. Update x1 = x0 - f(x0) / f'(x)
# 5. If |x1 - x0| < tolerance, return x1 as the root
# 6. If not, set x0 = x1 and repeat steps 3-5 until convergence or max iterations reached

import math
import matplotlib.pyplot as plt
import numpy as np
import os

# Define f(x) = e^x - 4x
def f(x):
    return math.exp(x) - 4*x

# Define f'(x) = derivative of f(x) = e^x - 4
def df(x):
    return math.exp(x) - 4

# Newton-Raphson Method
def newton_raphson(x0, tol=1e-5, max_iter=100):
    print(f"\n Starting Newton-Raphson Method:\nInitial guess: x0 = {x0}, tolerance = {tol}")
    results = []

    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print(" Derivative is zero. Cannot continue.")
            return None, results

        x1 = x0 - fx / dfx
        results.append((i+1, x0, fx, dfx, x1))

        print(f"Iteration {i+1}: x = {x0:.6f}, f(x) = {fx:.6f}, f'(x) = {dfx:.6f}, next x = {x1:.6f}")

        if abs(x1 - x0) < tol:
            print(f"\n Converged to root at x = {x1:.6f} after {i+1} iterations.")
            return x1, results

        x0 = x1

    print("\n Maximum iterations reached without convergence.")
    return None, results

# Save iteration data to file
def save_results(results, filename="results/newton_output.txt"):
    os.makedirs("results", exist_ok=True)
    with open(filename, "w") as f:
        f.write("Iter\t   x\t\tf(x)\tf'(x)\t   Next x\n")
        f.write("="*60 + "\n")
        for i, x, fx, dfx, x1 in results:
            f.write(f"{i}\t{x:.6f}\t{fx:.6f}\t{dfx:.6f}\t{x1:.6f}\n")
    print(f"\n Results saved to {filename}")

# graph
def plot_graph(results):
    x_vals = np.linspace(0, 2, 400)
    y_vals = [math.exp(x) - 4*x for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x) = e^x - 4x", color='blue')
    plt.axhline(0, color='red', linestyle='--', linewidth=0.8)

    for i, x, fx, dfx, x1 in results:
        plt.plot(x1, f(x1), 'ro')
        if i == len(results):
            plt.annotate(f"x ≈ {x1:.4f}", (x1, f(x1)), textcoords="offset points", xytext=(0,10), ha='center')

    plt.title("Newton-Raphson Method Convergence")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

# Main 
if __name__ == "__main__":
    print("\n==============================")
    print(" Newton-Raphson Method: Solve e^x = 4x")
    print("==============================\n")

    x0 = 1.0 # Initial guess
    root, results = newton_raphson(x0)

    if root is not None:
        save_results(results)
        plot_graph(results)
    else:
        print("No root found.")
