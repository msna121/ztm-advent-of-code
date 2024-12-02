level_dict = {}
filename = 'input_day2.txt'

def read_lists_from_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            level_list = line.split()
            yield list(map(int, level_list))

for i, level_list in enumerate(read_lists_from_file_generator(filename)):
    level_dict[i] = level_list

# print(level_dict)

def is_safe_with_one_removal(levels):
    """Checks if a list of levels can be made safe by removing at most one level.

    Args:
        levels: A list of integer levels.

    Returns:
        True if the list can be made safe, False otherwise.
    """

    if len(levels) <= 1:
        return True

    def is_monotonic_with_diff(nums):
        if len(nums) <= 1:
            return True
        direction = nums[1] - nums[0]
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff * direction <= 0 or abs(diff) > 3:
                return False
        return True
    
    # ----------------Part-2----------------- #
    # Check if the list is already safe
    if is_monotonic_with_diff(levels):
        return True

    # Try removing each level and check if the remaining list is safe
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_monotonic_with_diff(new_levels):
            return True

    return False
    # ----------------Part-2----------------- #

def count_safe_reports(reports):
    """Counts the number of safe reports in a list of reports.

    Args:
        reports: A list of lists of levels.

    Returns:
        The number of safe reports.
    """

    count = 0
    for report in reports.values():
        if is_safe_with_one_removal(report):
            count += 1
            # print('safe:', report)
    return count

# Example usage:
# data = {
#     0: [43, 47, 48, 50, 51, 52], 
#     1: [39, 41, 43, 45, 46, 46], 
#     2: [35, 38, 39, 41, 44, 47, 50, 54], 
#     3: [68, 69, 71, 74, 75, 78, 80, 87], 
#     4: [80, 82, 81, 82, 83, 85, 88], 
#     5: [48, 51, 54, 55, 58, 57, 55], 
#     6: [41, 44, 47, 50, 47, 47], 
#     7: [66, 68, 71, 70, 73, 77], 
#     8: [29, 32, 29, 30, 35]
# }

# safe_count = count_safe_reports(data)
# print("Number of safe reports:", safe_count)

safe_count = count_safe_reports(level_dict)
print("Number of safe reports:", safe_count)
