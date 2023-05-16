import os
import time

def animate(size, start_pattern, steps, interval):
    '''
    Main animation function. Creates grid of `size` and initializes with
    `start_pattern` and then displays `steps` frames of animation at 
    `interval` seconds between frames.
    '''
    # Make grid
    grid = make_grid(size)

    # Initialize with pattern
    grid = make_pattern(grid, start_pattern)

    # Animate
    for _ in range(steps):
        os.system('clear')
        display(grid)
        grid = next_grid(grid)
        time.sleep(interval)

def make_grid(size):
    '''
    Create grid of size (x, y) and initialize with 0.
    '''

    x, y = size
    grid = [[0 for _ in range(y)] for _ in range(x)]
    return grid


def next_grid(grid):
    '''
    Compute and return next grid state.
    '''

    x, y = len(grid), len(grid[0])

    next_grid = make_grid((x, y))

    for i in range(x):
        for j in range(y):
            next_grid[i][j] = next_square((i, j), grid)

    return next_grid

def next_square(coords, grid):
    '''
    Compute next square state based on sum of eight surrounding squares.
    '''
    x, y = coords

    neighbors = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x,   y-1),           (x,   y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]

    sum_neighbors = sum([grid[x][y] for x, y in neighbors if is_valid_coord(grid, (x, y))])

    if grid[x][y]:  # Rule for if the cell is alive
        return int(2 <= sum_neighbors <= 3)
    else:           # Rule for if the cell is dead
        return int(sum_neighbors == 3)

def is_valid_coord(grid, coords):
    '''
    Validate whether `coords` are in bounds of `grid`
    '''
    x, y = coords
    xmax, ymax = len(grid), len(grid[0])
    return 0 <= x < xmax and 0 <= y < ymax

def display(grid):
    '''
    Display `grid`
    '''
    x, y = len(grid), len(grid[0])
    for rownum in range(x):
        print(' '.join(['*' if val else ' '  for val in grid[rownum]]))

def make_pattern(grid, pattern):
    '''
    Initialize `grid` with `pattern`.
    '''
    for coord in pattern:
        x, y = coord
        grid[x][y] = 1
    return grid


if __name__ == '__main__':

    # Patterns
    glider = [(0, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
    blinker = [(1, 2), (2, 2), (3, 2)]
    light_ship = [
        (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 3), (2, 4),
        (3, 2), (3, 3)
    ]
    
    # Run animation
    animate(size=(40, 40), start_pattern=light_ship, steps=200, interval=.1)
