#approximate root of x^2= sinx by bisection method taking a=0.5, b=1.0
# f(x)= x^2 - sin(x)=0 
#ALGORITHM:
# 1. Check if f(a) and f(b) have opposite signs
# 2. Calculate midpoint c=(a+b)/2
# 3. If f(c) is close to zero, return c as the root
# 4. If f(c) has the same sign as f(a), update a=c
# 5. If f(c) has the same sign as f(b), update b=c
# 6. Repeat steps 2-5 until the desired tolerance is achieved
import math
import matplotlib.pyplot as plt
import numpy as np
import os

# Define the function f(x) = x^2 - sin(x)
def f(x):
    return x**2 - math.sin(x)

# Validate the initial interval
def validate_input(a, b):
    if a >= b:
        raise ValueError("a must be less than b")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    print("Input interval is valid.")
    return True

# Bisection Method
def bisection(a, b, tol=1e-5, max_iter=100):
    validate_input(a, b)
    results = []

    print(f"\nStarting Bisection Method:\na = {a}, b = {b}, tolerance = {tol}")
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        results.append((i+1, a, b, c, fc))

        print(f"Iteration {i+1}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6f}")

        if abs(fc) < tol:
            print(f"\n Converged to root at x = {c:.6f} after {i+1} iterations")
            return c, results

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("\n Maximum iterations reached without convergence.")
    return None, results

# Display results nicely and write to file
def save_results(results, filename="results/bisection_output.txt"):
    os.makedirs("results", exist_ok=True)
    with open(filename, "w") as f:
        f.write("Iteration\t   a\t\t   b\t\t   c\t\t f(c)\n")
        f.write("="*60 + "\n")
        for i, a, b, c, fc in results:
            line = f"{i:>5}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{fc:.6f}\n"
            f.write(line)
    print(f"\n Results saved to {filename}")

# Optional: plot f(x) and convergence points
def plot_graph(results):
    x_vals = np.linspace(0.4, 1.1, 400)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x) = x² - sin(x)", color='blue')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)

    for i, a, b, c, fc in results:
        plt.plot(c, fc, 'ro')  # Midpoint
        if i == len(results):
            plt.annotate(f"root ≈ {c:.4f}", (c, fc), textcoords="offset points", xytext=(0,10), ha='center')

    plt.title("Bisection Method Convergence")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

# Main
if __name__ == "__main__":
    print("\n==============================")
    print(" Bisection Method: Solve x² = sin(x)")
    print("==============================\n")
    
    a = 0.5
    b = 1.0
    root, results = bisection(a, b)

    if root is not None:
        save_results(results)
        plot_graph(results)
    else:
        print("No root found within the specified interval.")
