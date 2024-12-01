# Part-1
list1 = []
list2 = []
filename = 'input_day1.txt'

def read_lists_from_file_generator(filename, delimiter='  '):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(delimiter)
            yield int(parts[0]), int(parts[1])

for num1, num2 in read_lists_from_file_generator(filename):
    list1.append(num1)
    list2.append(num2)

# print(list1)
# print(list2)

def distance_calculator(loc_id1: list[int], loc_id2: list[int]) -> int:
    loc_id1 = sorted(loc_id1)
    loc_id2 = sorted(loc_id2)
    distance = sum([abs(x-y) for x,y in zip(loc_id1, loc_id2)])
    return distance

# a = [1,2,3]
# b = [2,3,3]

# print(distance_calculator(a,b))

print(distance_calculator(list1, list2))


# Part-2
def calculate_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts.get(num, 0)

    return similarity_score

# Example usage:
# left_list = [3, 4, 2, 1, 3, 3]
# right_list = [4, 3, 5, 3, 9, 3]

# score = calculate_similarity_score(left_list, right_list)
# print("Similarity score:", score)

print(calculate_similarity_score(list1, list2))