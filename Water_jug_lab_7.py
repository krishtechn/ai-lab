from collections import deque

def water_jug_problem(jug1, jug2, goal):
    visited = set()
    queue = deque()

    queue.append((0, 0))   # initial state

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        print(f"({x}, {y})")

        visited.add((x, y))

        # Goal check
        if x == goal or y == goal:
            print("\nGoal reached!")
            return

        # Possible operations:

        # 1. Fill Jug1
        queue.append((jug1, y))

        # 2. Fill Jug2
        queue.append((x, jug2))

        # 3. Empty Jug1
        queue.append((0, y))

        # 4. Empty Jug2
        queue.append((x, 0))

        # 5. Pour Jug1 → Jug2
        new_x = max(0, x - (jug2 - y))
        new_y = min(jug2, y + x)
        queue.append((new_x, new_y))

        # 6. Pour Jug2 → Jug1
        new_x = min(jug1, x + y)
        new_y = max(0, y - (jug1 - x))
        queue.append((new_x, new_y))


# Example: Jug1 = 4L, Jug2 = 3L, Goal = 2L
water_jug_problem(4, 3, 2)




