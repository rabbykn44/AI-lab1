# Write a Python program to get the 4th element from the beginning and the 4th element from the last of
# a tuple.
# 1 Sample Input:
# 2 tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# 3 Sample Output:
# 4 e,u


def get_fourth_elements(tuplex):
    # Get the 4th element from the beginning
    fourth_from_beginning = tuplex[3]
    # Get the 4th element from the end
    fourth_from_end = tuplex[-4]
    return fourth_from_beginning, fourth_from_end

def main():
    # Taking input from the user for the tuple
    elements = input("Enter elements of the tuple separated by commas: ")
    user_tuple = tuple(elements.split(','))

    # Get the 4th elements
    fourth_elements = get_fourth_elements(user_tuple)

    # Output
    print("4th element from the beginning and 4th element from the end:", fourth_elements)

if __name__ == "__main__":
    main()


# Enter elements of the tuple separated by commas: "w", 3, "r", "e", "s", "o", "u", "r", "c", "e"
# 4th element from the beginning and 4th element from the end: (' "e"', ' "u"')