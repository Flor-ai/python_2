def convert_time_duration():
    try:
        # Input the time duration in hours
        hours = float(input("Enter the time duration in hours: "))

        # Check if the entered time is non-negative
        if hours < 0:
            print("Error: Time duration must be a non-negative number.")
        return
        # Convert hours to minutes and seconds
        minutes = hours * 60
        seconds = hours * 3600
        # Display the converted time duration
        print(f"The time duration is: {minutes:.2f} minutes or {seconds:.2f}
        seconds.")
    except ValueError:
        # Handle non-numeric inputs
        print("Error: Please enter a valid numeric value for the time duration.")
        # Call the function
convert_time_duration()