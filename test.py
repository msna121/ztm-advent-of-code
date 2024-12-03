# aoc-day3
import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

text = "This is a text with mul(12,34) and mul(5,6) and some other mul(999,1) patterns."

matches = re.findall(pattern, text)

print(matches)

total_product = 0
for match in matches:
    num1, num2 = int(match[0]), int(match[1])
    print(num1, num2)
    total_product += num1 * num2
    print(total_product)