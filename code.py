import math
def inflation_adjusted_value(amount, year1, year2, inflation_rate):
    difference = year2 - year1
    adjusted_value = amount * ((1 + inflation_rate / 100) ** difference)
    return adjusted_value

def main():
    print("Inflation-Adjusted Value Calculator")
    try:
        amount = float(input("Enter the starting amount: "))
        year1 = int(input("Enter the starting year: "))
        year2 = int(input("Enter the target year: "))
        inflation_rate = float(input("Enter the average annual inflation rate (in %): "))

        if year1 > year2:
            print("The starting year must be less than or equal to the target year.")
            return

        adjusted_value = inflation_adjusted_value(amount, year1, year2, inflation_rate)
        print(f"The inflation-adjusted value of ${amount:,.2f} from {year1} to {year2} is: ${adjusted_value:,.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the amount, years, and inflation rate.")

if __name__ == "__main__":
    main()
