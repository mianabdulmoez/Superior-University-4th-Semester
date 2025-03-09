def water_jug(capacity_a, capacity_b, target):
    def get_next_states(state):
        a, b = state
        next_states = []
        next_states.append((capacity_a, b))
        next_states.append((a, capacity_b))
        next_states.append((0, b))
        next_states.append((a, 0))
        pour_amount = min(a, capacity_b - b)
        next_states.append((a - pour_amount, b + pour_amount))
        pour_amount = min(b, capacity_a - a)
        next_states.append((a + pour_amount, b - pour_amount))
        return next_states

    visited = {}
    stack = []
    initial_state = (0, 0)
    stack.append((initial_state, [initial_state]))

    while stack:
        current_state, path = stack.pop()
        if current_state[0] == target or current_state[1] == target:
            return path
        if current_state not in visited:
            visited[current_state] = True
            for next_state in get_next_states(current_state):
                if next_state not in visited:
                    stack.append((next_state, path + [next_state]))
    return None

def solution(solution):
    if solution:
        print("Solution steps:")
        for step_number, step in enumerate(solution):
            print(f"Step {step_number + 1}: Jug A: {step[0]}, Jug B: {step[1]}")
        print(f"Total steps: {len(solution)}")
    else:
        print("No solution exists.")

capacity_a = int(input("Enter capacity of Jug A: "))
capacity_b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter the desired amount of water: "))

if capacity_a <= 0 or capacity_b <= 0 or target <= 0:
    print("Invalid input! Capacities and target must be positive integers.")
else:
    n_solution = water_jug(capacity_a, capacity_b, target)
    solution(n_solution)