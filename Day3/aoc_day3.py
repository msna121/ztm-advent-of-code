import re

filename = 'input_day3.txt'

with open(filename, 'r') as file:
    data = file.read()

# Part-1
def calculate_multiplications(text):
    """Calculates the sum of products from 'mul(x, y)' patterns in the text.

    Args:
        text: The input text.

    Returns:
        The sum of products.
    """

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)

    total_product = 0
    for match in matches:
        num1, num2 = int(match[0]), int(match[1])
        total_product += num1 * num2

    return total_product

# Example usage:
# text = "This is a text with mul(12,34) and mul(5,6) and some other mul(999,1) patterns."
# result = calculate_multiplications(text)
# print(result)  # Output: 1437

part1_result = calculate_multiplications(data)
print(part1_result)

# Part-2
def calculate_multiplications_with_control(text):
    """Calculates the sum of products from 'mul(x, y)' patterns in the text, considering 'do()' and 'don't()' instructions.

    Args:
        text: The input text.

    Returns:
        The sum of products.
    """

    pattern = r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)

    mul_enabled = True
    total_product = 0
    for match in matches:
        if match[0] == "do()":
            mul_enabled = True
        elif match[0] == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                num1, num2 = int(match[1]), int(match[2])
                total_product += num1 * num2

    return total_product

# Example usage:
# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# result = calculate_multiplications_with_control(text)
# print(result)  # Output: 48

part2_result = calculate_multiplications_with_control(data)
print(part2_result)