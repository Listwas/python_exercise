#Ask the user for a numerator and a denominator. Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).


try:
    numerator = float(input("numerator: "))
    denominator = float(input("denominator: "))
    
    if denominator == 0:
        print("error: don't divide by zero!")
    else:
        percentage = (numerator / denominator) * 100
        print(f"percentage: {percentage:.2f}%")
except ValueError:
    print("wrong input")
