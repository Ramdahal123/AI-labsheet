import random
import time

def print_grid(grid, current_pos=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if current_pos and (i, j) == current_pos:
                print("P", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()

def main():
    x = int(input("Enter the Size of the Grid (x): "))
    y = int(input("Enter the Size of the Grid (y): "))

    # Initialize grid with random 0s and 1s
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]

    print("\nRandomly assigned grid states:")
    print_grid(grid)

    # Initial position
    initial_pos = [random.randint(0, x - 1), random.randint(0, y - 1)]
    print(f"\nInitial Position in the Grid: Room[{initial_pos[0]}, {initial_pos[1]}] => {grid[initial_pos[0]][initial_pos[1]]}")

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    steps = 0
    while True:
        i, j = initial_pos
        if grid[i][j] == 1:
            grid[i][j] = 0
            steps += 1
            print(f"Step {steps}: Room[{i}, {j}] was dirty. Cleaned it.")
        else:
            moved = False
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < x and 0 <= nj < y and grid[ni][nj] == 1:
                    initial_pos = [ni, nj]
                    steps += 1
                    print(f"Step {steps}: Current room clean. Moved to dirty neighbor Room[{ni}, {nj}].")
                    moved = True
                    break

            if not moved:
                found = False
                for i in range(x):
                    for j in range(y):
                        if grid[i][j] == 1:
                            initial_pos = [i, j]
                            steps += 1
                            print(f"Step {steps}: No dirty neighbor. Moving to Room[{i}, {j}].")
                            found = True
                            break
                    if found:
                        break

                if not found:
                    print(f"\nAll rooms are clean! Cleaning completed in {steps} steps.")
                    break

    print("\nFinal grid state:")
    print_grid(grid, tuple(initial_pos))

if __name__ == "__main__":
    main()
