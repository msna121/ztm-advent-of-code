import re

filename = 'input_day4.txt'

with open(filename, 'r') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def count_xmas_part1(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)

    # Directions: (dx, dy)
    directions = [
        (0, 1),    # Horizontal right
        (0, -1),   # Horizontal left
        (1, 0),    # Vertical down
        (-1, 0),   # Vertical up
        (1, 1),    # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),   # Diagonal down-left
        (-1, 1),   # Diagonal up-right
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for k in range(word_length):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if find_word(i, j, dx, dy):
                    count += 1

    return count

# Example grid
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

# Convert grid to a list of lists
grid = [list(row) for row in grid]

# Count occurrences of "XMAS"
result = count_xmas_part1(grid)
print("Number of XMAS occurrences:", result)

# Example usage:
# puzzle = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX"
# ]

# result = count_xmas(puzzle)
# print("Number of 'XMAS' occurrences:", result)

result_part1 = count_xmas_part1(data)
print("Number of 'XMAS' occurrences part-1:", result_part1)

def count_xmas_part2(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Define the "X-MAS" pattern relative to the center of the X
    xmas_offsets = [
        [(-1, -1), (0, 0), (1, 1)],  # Top-left to bottom-right MAS
        [(1, -1), (0, 0), (-1, 1)]   # Bottom-left to top-right MAS
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def matches_mas(x, y, offsets):
        """Check if the positions form a valid MAS sequence."""
        mas_sequence = ""
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if not is_valid(nx, ny):
                return False
            mas_sequence += grid[nx][ny]
        # Check for MAS or SAM pattern
        return mas_sequence in ("MAS", "SAM")

    def find_xmas(x, y):
        """Check if an X-MAS pattern exists centered at (x, y)."""
        if grid[x][y] != "A":
            return False
        for offsets in xmas_offsets:
            if not matches_mas(x, y, offsets):
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            if find_xmas(i, j):
                count += 1

    return count

# Example grid
# grid = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX",
# ]

# # Convert grid to a list of lists
# grid = [list(row) for row in grid]

# # Count occurrences of "X-MAS"
# result = count_xmas(grid)
# print("Number of X-MAS occurrences:", result)

result_part2 = count_xmas_part2(data)
print("Number of 'XMAS' occurrences part-2:", result_part2)
