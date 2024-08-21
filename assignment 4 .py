import math
def calculate_distance():
    try:
        # Input coordinates of the first point
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))
        # Input coordinates of the second point
        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))
        # Calculate the distance between the two points
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # Display the calculated distance
        print(f"The distance between the two points is: {distance:.2f}")
    except ValueError:
        # Handle non-numeric inputs
        print("Error: Please enter valid numeric values for the coordinates.")
        # Call the function
calculate_distance()