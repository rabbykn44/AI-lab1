# Write a python program to find the sum of the numbers passed as parameters.
def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

def main():
    numbers = input("Enter the numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    
    result = find_sum(*numbers)
    
    print("The sum of the numbers is:", result)

if __name__ == "__main__":
    main()

# Enter the numbers separated by spaces: 10 20 30 50
# The sum of the numbers is: 110.0