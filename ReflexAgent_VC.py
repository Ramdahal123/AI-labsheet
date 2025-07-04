import random

def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))

def all_clean(grid):
    for row in grid:
        if 1 in row:
            return False
    return True

def main():
    x = int(input("Enter the Size of the Grid (x): "))
    y = int(input("Enter the Size of the Grid (y): "))

    # Create grid with random states: 0 = clean, 1 = dirty
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]

    print("\nInitial grid state:")
    print_grid(grid)

    # Random initial position
    posX = random.randint(0, x - 1)
    posY = random.randint(0, y - 1)
    steps = 0

    print(f"\nInitial Position: Room[{posX}, {posY}]")

    while True:
        if grid[posX][posY] == 1:
            grid[posX][posY] = 0
            steps += 1
            print(f"Step {steps}: Cleaned Room[{posX}, {posY}].")
        else:
            # Move randomly to an adjacent cell
            while True:
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
                newX = posX + dx
                newY = posY + dy
                if 0 <= newX < x and 0 <= newY < y:
                    break
            posX = newX
            posY = newY
            steps += 1
            print(f"Step {steps}: Moved to Room[{posX}, {posY}].")

        # Check if all rooms are clean
        if all_clean(grid):
            break

    print(f"\nAll rooms clean! Total steps = {steps}")

if __name__ == "__main__":
    main()
