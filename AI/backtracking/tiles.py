def solve_8_tiles(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    visited = set()
    path = []

    def is_valid(state):
        return tuple(map(tuple, state)) not in visited

    def is_goal(state):
        return state == goal_state

    def get_neighbors(state):
        neighbors = []
        zero_position = find_zero(state)
        if zero_position is not None:
            zero_row, zero_col = zero_position
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = zero_row + dr, zero_col + dc
                if 0 <= new_row < 3 and 0 <= new_col < 3:
                    new_state = [row[:] for row in state]
                    new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                    neighbors.append(new_state)

        return neighbors

    def find_zero(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def backtrack(state):
        visited.add(tuple(map(tuple, state)))

        if is_goal(state):
            return True

        for neighbor in get_neighbors(state):
            if is_valid(neighbor):
                path.append(neighbor)
                if backtrack(neighbor):
                    return True
                path.pop()

        return False

    path.append(initial_state)
    if backtrack(initial_state):
        return path
    else:
        return None

# Example usage:
initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
solution = solve_8_tiles(initial_state)
if solution:
    print("Solution found!")
    for state in solution:
        print(state)
else:
    print("No solution found.")
