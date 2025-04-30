def length_converter():
    print("\nLength Units: meters (m), kilometers (km), miles (mi), feet (ft)")
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    # Convert from any to meters
    to_meters = {
        "m": 1,
        "km": 1000,
        "mi": 1609.34,
        "ft": 0.3048
    }

    if from_unit not in to_meters or to_unit not in to_meters:
        print("Invalid unit.")
        return

    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def weight_converter():
    print("\nWeight Units: kilograms (kg), grams (g), pounds (lb), ounces (oz)")
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    to_kg = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592,
        "oz": 0.0283495
    }

    if from_unit not in to_kg or to_unit not in to_kg:
        print("Invalid unit.")
        return

    kg = value * to_kg[from_unit]
    result = kg / to_kg[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def temperature_converter():
    print("\nTemperature Units: Celsius (C), Fahrenheit (F), Kelvin (K)")
    value = float(input("Enter value: "))
    from_unit = input("From unit (C/F/K): ").upper()
    to_unit = input("To unit (C/F/K): ").upper()

    if from_unit == to_unit:
        print(f"{value} {from_unit} = {value} {to_unit}")
        return

    if from_unit == "C":
        if to_unit == "F":
            result = (value * 9/5) + 32
        elif to_unit == "K":
            result = value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            result = (value - 32) * 5/9
        elif to_unit == "K":
            result = (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            result = value - 273.15
        elif to_unit == "F":
            result = (value - 273.15) * 9/5 + 32
    else:
        print("Invalid unit.")
        return

    print(f"{value} {from_unit} = {result:.2f} {to_unit}")

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Choose a category (1-4): ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()