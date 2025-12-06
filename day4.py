def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    # All 8 neighbor directions
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # Check inside grid
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbors += 1

            if neighbors < 4:
                accessible += 1

    return accessible

with open("input4.txt") as f:
    grid = [line.strip() for line in f]

print(count_accessible_rolls(grid))


#----------------------------------------------------------


def total_removed_rolls(grid):
    grid = [list(row) for row in grid]
    rows, cols = len(grid), len(grid[0])

    dirs = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),         (0,1),
        (1,-1), (1,0),  (1,1)
    ]

    total_removed = 0

    while True:
        to_remove = []

        # 1. Find accessible rolls
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue

                neighbors = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbors += 1

                if neighbors < 4:
                    to_remove.append((r, c))

        # 2. Stop if no more rolls can be removed
        if not to_remove:
            break

        # 3. Remove them
        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed

print(total_removed_rolls(grid))

