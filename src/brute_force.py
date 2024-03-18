import matplotlib.pyplot as plt
import time

def bezier_curve_recursive(control_points, t):
    """ Recursively calculates the Bezier curve point at a specific t """
    if len(control_points) == 1:
        return control_points[0]
    new_points = []
    for i in range(len(control_points) - 1):
        new_x = control_points[i][0] * (1 - t) + control_points[i + 1][0] * t
        new_y = control_points[i][1] * (1 - t) + control_points[i + 1][1] * t
        new_points.append((new_x, new_y))
    return bezier_curve_recursive(new_points, t)

def plot_bezier_brute_force(control_points, iterations):
    """ Plots the Bezier curve for a given set of control points """
    start_time = time.time()
    num_points = pow(2, iterations)+1 + pow(2, iterations-1)*(len(control_points)-3) 
    bezier_points = [bezier_curve_recursive(control_points, t/num_points) for t in range(num_points + 1)]
    # Extract x and y coordinates from points
    x_values, y_values = zip(*bezier_points)
    control_x, control_y = zip(*control_points)

    plt.figure()
    plt.plot(x_values, y_values, 'b-', label='Bezier Curve')
    plt.plot(control_x, control_y, 'ro--', label='Control Points', color='green')
    # bezier_x, bezier_y = zip(*bezier_points)
    # plt.scatter(bezier_x, bezier_y, color='red', label='Bezier Points', s=0.5)
    plt.title('Bezier Curve with Brute Force Algorithm')
    plt.legend()

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nExecution time: {execution_time:.2f} ms")

    plt.show()

def display_welcome_message():
    print("================================================")
    print("  Welcome to the Bézier Curve Animator ✨✨✨ ")
    print("================================================")
    print("\nThis program allows you to animate the formation of Bézier curves using the Brute Force method.")
    print("\nPlease follow the prompts to input your control points.")
    print("\nLet's get started!\n")

def main():
    display_welcome_message()
    # Take input from the user for the control points
    control_points = []
    n = int(input("Enter the number of control points: "))
    if n < 2:
        print("At least 2 control points are required to form a Bezier curve.")
        return
    for i in range(n):
        x, y = map(float, input(f"Enter the x and y coordinates of point {i + 1}: ").split())
        control_points.append((x, y))
    
    # Plot the Bezier curve
    iterations = int(input("Enter the number of iterations: "))
    plot_bezier_brute_force(control_points, iterations)
    
    print("\nGoodbye! Hope you enjoyed the bezier curve 💞")

if __name__ == "__main__":
    main()