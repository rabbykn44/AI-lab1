def swap_tuples(tuple1, tuple2):
    return tuple2, tuple1

def main():
    # Taking input from the user for tuple1
    tuple1_input = input("Enter elements for tuple1 separated by commas: ")
    tuple1 = tuple(map(int, tuple1_input.split(',')))

    # Taking input from the user for tuple2
    tuple2_input = input("Enter elements for tuple2 separated by commas: ")
    tuple2 = tuple(map(int, tuple2_input.split(',')))

    # Swapping the tuples
    tuple1, tuple2 = swap_tuples(tuple1, tuple2)

    # Output
    print("tuple1:", tuple1)
    print("tuple2:", tuple2)

if __name__ == "__main__":
    main()

# Enter elements for tuple1 separated by commas: 11,22
# Enter elements for tuple2 separated by commas: 99,88
# tuple1: (99, 88)
# tuple2: (11, 22)