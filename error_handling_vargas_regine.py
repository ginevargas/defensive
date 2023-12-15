# CSEC 311 - DEFENSIVE PROGRAMMING
# Error Exception - Activity
# Vargas, Regine B.
# bscs3A

import math

def calculator():
    previous_results = {}   # dictionary to store previous results 

    while True:
        try:
            num1 = input("Enter the first number (or 'q' to quit): ") # get user input for the first number
            if num1.lower() == 'q':
                break
            
            num1 = float(num1)  # convert the first number to a float

            num2 = float(input("Enter the second number: ")) # get user input for the second number
            # get user input for the operation
            operation = input("Enter the operation (+, -, *, /, ** for exponentiation, sqrt for square root): ")
            # check if the operation is valid
            if operation not in ['+', '-', '*', '/', '**', 'sqrt']:
                raise ValueError("Invalid operation.")
            # check for division by zero
            if operation == '/' and num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            # check for square root of a negative number
            if operation == 'sqrt' and num1 < 0:
                raise ValueError("Cannot calculate square root of a negative number.")
            # perform the calculation based on the user's input
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == 'sqrt':
                result = math.sqrt(num1)

        except ValueError as ve:
            print(f"Error: {ve}")    # handle ValueErrors for invalid input or square root of a negative number
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")   # handle ZeroDivisionError for division by zero
        except Exception as e:
            print(f"An unexpected error occurred: {e}") # handle other unexpected exceptions
        else:
            print(f"\nResult: {result}")  # print the result if no exceptions are raised
            previous_results[(num1, num2, operation)] = result  # store the result in the dictionary for future reference
        finally:
            if num1 != 'q': # check if the user entered 'q' to quit before printing the message
                print("This block always executes, whether an exception occurred or not.\n")

    # display previous results after exiting the calculator loop
    print("\nPrevious Results:")
    for key, value in previous_results.items():
        print(f"{key} => {value}")

if __name__ == "__main__":
    calculator() # call the calculator function if the script is run as the main program
