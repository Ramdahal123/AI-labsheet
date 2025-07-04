import random

def abs_val(a):
    return -a if a < 0 else a

def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))

def main():
    x = int(input("Enter the Size of the Grid (x): "))
    y = int(input("Enter the Size of the Grid (y): "))

    # Initialize grid with 0 (clean) or 1 (dirty)
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]

    print("\nInitial grid state:")
    print_grid(grid)

    # Random starting position
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
            # Find the nearest dirty room using Manhattan distance
            minDist = float('inf')
            targetX, targetY = -1, -1

            for i in range(x):
                for j in range(y):
                    if grid[i][j] == 1:
                        dist = abs_val(i - posX) + abs_val(j - posY)
                        if dist < minDist:
                            minDist = dist
                            targetX, targetY = i, j

            if targetX == -1:
                break  # No dirty rooms left

            # Move one step toward the nearest dirty room
            if targetX > posX:
                posX += 1
            elif targetX < posX:
                posX -= 1
            elif targetY > posY:
                posY += 1
            elif targetY < posY:
                posY -= 1

            steps += 1
            print(f"Step {steps}: Moved to Room[{posX}, {posY}].")

    print(f"\nAll rooms clean! Total steps = {steps}")

if __name__ == "__main__":
    main()
