def currency_converter():
    # Define fixed exchange rates (for demonstration purposes)
    exchange_rates = {
    "USD to EUR": 0.85,
    "USD to GBP": 0.75,
    "EUR to USD": 1.18,
    "GBP to USD": 1.33
    }
    # Display available currency pairs
    print("Available currency pairs:")
    for pair in exchange_rates.keys():
        print(pair)
        try:
            # Ask the user to choose a currency pair
            currency_pair = input("Enter the currency pair you want to convert (e.g., USD to EUR): ")

            # Validate the currency pair
            if currency_pair not in exchange_rates:
                print("Error: Invalid currency pair. Please choose from the available pairs.")
            return
            # Ask the user to enter the amount in the source currency
            amount = float(input(f"Enter the amount in {currency_pair.split(' ')[0]}:"))
            # Ensure the amount is non-negative
            if amount < 0:
                print("Error: Amount must be a non-negative number.")
            return
            # Convert the amount using the exchange rate
            converted_amount = amount * exchange_rates[currency_pair]
            # Display the converted amount
            print(f"The converted amount in {currency_pair.split(' ')[2]} is:
            {converted_amount:.2f}")
        except ValueError:
            # Handle non-numeric input for the amount
            print("Error: Please enter a valid numeric value for the amount.")
            # Call the function
currency_converter()