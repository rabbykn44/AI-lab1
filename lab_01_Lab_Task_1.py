# Write a python program to find the largest number between two numbers using function
def find_largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def find_largest_between_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    largest = find_largest(num1, num2)
    
    print("The largest number is:", largest)

if __name__ == "__main__":
    find_largest_between_two_numbers()


# Enter the first number: 12
# Enter the second number: 24
# The largest number is: 24.0
