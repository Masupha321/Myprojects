numbers_list = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8]

unique_numbers = set(numbers_list)
print("Unique numbers:", unique_numbers)

total_sum = sum(unique_numbers)
print("Sum of unique numbers:", total_sum)

max_num = max(unique_numbers)
min_num = min(unique_numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

unique_numbers.remove(max_num)
print("Updated set after removing the largest number:", unique_numbers)

new_numbers = {4, 5, 6, 9, 10}

union_result = unique_numbers.union(new_numbers)
print("Union:", union_result)

intersection_result = unique_numbers.intersection(new_numbers)
print("Intersection:", intersection_result)

difference_result = unique_numbers.difference(new_numbers)
print("Difference (unique_numbers - new_numbers):", difference_result)

symmetric_difference_result = unique_numbers.symmetric_difference(new_numbers)
print("Symmetric Difference:", symmetric_difference_result)

