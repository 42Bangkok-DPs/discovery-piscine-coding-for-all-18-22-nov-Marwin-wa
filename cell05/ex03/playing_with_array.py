original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []
for number in original_array:
    if number > 5:
        new_array.append(number + 2)

unique_values = set(new_array)

print(original_array)
print(unique_values)
