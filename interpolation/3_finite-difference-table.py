#construct finite difference table of f(x)=e^x on interval -1<=x<=1 by dividing interval by equally space points of step size 0.1
#algorithm:
# 1. Define the function f(x) = e^x
# 2. Generate x values from -1 to 1 with step size 0.1
# 3. Calculate f(x) for each x value
# 4. Create a finite difference table using the calculated f(x) values

import math
import numpy as np
import matplotlib.pyplot as plt
import os 


def f(x):
    return math.exp(x)

#  x-values from -1 to 1 with step 0.1
def generate_x_values(start=-1.0, end=1.0, step=0.1):
    return [round(start + i * step, 2) for i in range(int((end - start) / step) + 1)]

# forward difference table
def finite_difference_table(x_values):
    y = [f(x) for x in x_values]
    table = [y.copy()]  # 0th order differences

    for level in range(1, len(x_values)):
        prev = table[level - 1]
        curr = [round(prev[i + 1] - prev[i], 6) for i in range(len(prev) - 1)]
        table.append(curr)

    return table

# Print the difference table
def display_table(x_values, table):
    print("Finite Difference Table for f(x) = e^x")
    print("x      f(x)     " + "".join([f"D{level+1:<10}" for level in range(1, len(table))]))
    print("=" * 120)

    for i in range(len(x_values)):
        row = f"{x_values[i]:<6.2f} {table[0][i]:<10.6f}"
        for level in range(1, len(table)):
            if i < len(table[level]):
                row += f"{table[level][i]:<10.6f}"
            else:
                row += " " * 10
        print(row)
    
# Save to file
def save_table(x_values, table, filename="results/finite-difference-table.txt"):
    os.makedirs("results", exist_ok=True)
    with open(filename, "w", encoding='utf-8') as f:
        f.write("x      f(x)     " + "".join([f"D{level+1:<10}" for level in range(1, len(table))]) + "\n")
        f.write("=" * 120 + "\n")
        for i in range(len(x_values)):
            row = f"{x_values[i]:<6.2f} {table[0][i]:<10.6f}"
            for level in range(1, len(table)):
                if i < len(table[level]):
                    row += f"{table[level][i]:<10.6f}"
                else:
                    row += " " * 10
            f.write(row + "\n")
    print(f"\n Table saved to {filename}")


# plot f(x) and finite difference points
def plot_graph(x_values, table):
    x = np.linspace(-1, 1, 100)
    y = [f(xi) for xi in x]
    plt.plot(x, y, label='f(x) = e^x', color='pink')
    for i in range(1):
        y_diff = [table[i][j] if j < len(table[i]) else None for j in range(len(x_values))]
        plt.scatter(x_values, y_diff, label='f(x) points', color='red', marker='o')

    plt.title("Finite Difference Table Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
    print("Plot displayed above.")

# Main function
if __name__ == "__main__":
    print("\n====================================")
    print(" Finite Difference Table: f(x) = e^x")
    print("Interval: -1 to 1, Step size = 0.1")
    print("====================================\n")
    x_vals = generate_x_values(-1.0, 1.0, 0.1)
    table = finite_difference_table(x_vals)

    display_table(x_vals, table)
    save_table(x_vals, table)
    plot_graph(x_vals, table)
