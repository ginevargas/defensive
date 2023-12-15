# Defensive Programming
# creating three functions to calculate the Fibonacci number at the Nth position using different approaches.


def first_approach(n):    # first approach to compute fibonacci
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def second_approach(n):  # second approach to compute fibonacci
    if (n <= 1):
        return n
    else:
        return (second_approach(n - 1) + second_approach(n - 2))

def third_approach(n):  # third approach to compute fibonacci
    if n in {0, 1}:
        return n
    return third_approach(n - 1) + third_approach(n - 2)


if __name__ == "__main__": 
    print("+----------------------------------------------------------------------------------------+")
    print("| Fibonacci Numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 |")
    print("| The nth position: ", end=" ")
    
    for i in range(1, 18):
        print(i, end=", " if i < 17 else "           |")
    print("\n+----------------------------------------------------------------------------------------+")

    
    n = int(input("Enter the value of N (positive integer): "))
    if n >= 1:
        print("Using 1st Approach: ", first_approach(n))
        print("Using 2nd Approach: ", second_approach(n))
        print("Using 3rd Approach: ", third_approach(n))

    else:
        print("Error: Nth position must be a positive integer") 
        # If input is not a positive integer it displays an error message: "Error: Nth position must be a positive integer."
        
    file1 = open(r'C:\Users\Regine Vargas\Documents\Vs code\act1_output', 'w')
    file1.write('1\n')
    for i in range(2, n+1):
        file1.write(str(first_approach(i))+'\n')
    file1.close()
