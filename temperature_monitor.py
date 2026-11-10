# TEMPERATURE MONITOR AND ALARM CHECKER
# ND1 Mechatronics Engineering, YabaTech

def temperature_monitor():

    print("===================================")
    print(" TEMPERATURE MONITOR AND ALARM")
    print("===================================")

    # Example safe temperature limit
    safe_limit = 60

    # Store temperature readings
    temperatures = []

    # Collect five valid temperature readings
    for i in range(5):
        while True:
            try:
                reading = float(input(f"Enter temperature {i + 1} in Celsius: "))
                temperatures.append(reading)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Display all readings
    print("\nAll temperature readings:", temperatures)

    # Calculate temperature statistics
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    # Display results
    print("\n========== RESULTS ==========")
    print("Highest temperature:", highest, "°C")
    print("Lowest temperature:", lowest, "°C")
    print("Average temperature:", round(average, 2), "°C")

    # Check machine status
    if highest > safe_limit:
        print("\nWARNING: Temperature is too high!")
        print("Machine status: CRITICAL")
    else:
        print("\nMachine status: NORMAL")

    # Identify readings above the limit
    print("\nChecking individual readings:")

    for i in range(len(temperatures)):
        if temperatures[i] > safe_limit:
            print("Alert: Reading", i + 1, "is too high!")

    print("\nTemperature monitoring complete.")


# Run the program
temperature_monitor()