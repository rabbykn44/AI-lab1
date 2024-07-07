# Write a Python Program to Count Even and Odd Numbers in a list.
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

def main():
    # Taking input from the user for the list of numbers
    elements = input("Enter elements of the list separated by commas: ")
    user_list = list(map(int, elements.split(',')))

    # Count even and odd numbers
    even_count, odd_count = count_even_odd(user_list)

    # Output
    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)

if __name__ == "__main__":
    main()

# Enter elements of the list separated by commas: 1,2,3,4,5,6,7,8,9,10,11
# Number of even numbers: 5
# Number of odd numbers: 6