# • Write a program to perform graph coloring algorithm which take input as text file from computer.
def read_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            nodes = line.strip().split()
            vertex = nodes[0]
            neighbors = nodes[1:]
            adjacency_list[vertex] = neighbors
    return adjacency_list

def graph_coloring(adj_list, num_of_colors):
    colors = {node: 0 for node in adj_list}  # Initialize all colors to 0 (no color)
    
    def solve(v):
        if v is None:  # Base case: all nodes are colored
            return True
        for c in range(1, num_of_colors + 1):
            if is_possible(v, c):
                colors[v] = c
                if solve(next_node(v)):
                    return True
                colors[v] = 0  # Backtrack
        return False

    def is_possible(v, c):
        for neighbor in adj_list[v]:
            if colors.get(neighbor) == c:
                return False
        return True

    def next_node(v):
        for node in adj_list:
            if colors[node] == 0:  # Find an uncolored node
                return node
        return None

    def display():
        text_color = ["", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PINK",
                      "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"]
        print("Colors:")
        for node, color_index in colors.items():
            print(f"{node}: {text_color[color_index]}")

    if solve(next(iter(adj_list))):
        print("\nSolution exists")
        display()
    else:
        print("No solution exists with the given number of colors")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file containing the adjacency list: ")
    num_colors = int(input("Enter the number of colors: "))
    
    adj_list = read_adjacency_list(file_path)
    graph_coloring(adj_list, num_colors)
