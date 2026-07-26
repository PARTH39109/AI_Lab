from copy import deepcopy

# Initial State
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Goal State
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


# Find the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Convert state into tuple (for storing in visited set)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


# Generate all possible next states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    # Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)

            # Swap blank with adjacent tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


# Depth First Search
def dfs(initial, goal):
    stack = [(initial, [])]  # (current_state, path)
    visited = set()

    while stack:
        current, path = stack.pop()

        if state_to_tuple(current) in visited:
            continue

        visited.add(state_to_tuple(current))

        new_path = path + [current]

        if current == goal:
            return new_path

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                stack.append((neighbor, new_path))

    return None


# Print solution
solution = dfs(initial_state, goal_state)

if solution:
    print("Solution Found!\n")

    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")