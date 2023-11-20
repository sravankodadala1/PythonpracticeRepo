num_list = [1, 2, 3, 4, 5]

# Access a single element
print(num_list[0])  # Output: 1
 
# Slicing to get a sublist
print(num_list[1:3])  # Output: [2, 3]
 
num_list[3] = 9
print(num_list)  # Output: [1, 2, 3, 9, 5]

# Append an element to the end
num_list.append(6)

# Insert an element at a specific index
num_list.insert(2, 7)

# Extend the list with another list
num_list.extend([8, 9])

print(num_list)  # Output: [1, 2, 7, 10, 4, 5, 6, 8, 9]

# Remove element by value
num_list.remove(7)

# Remove element by index
popped_value = num_list.pop(3)

# Remove all elements
num_list.clear()

print(num_list)  # Output: []

# Find index of an element
index = num_list.index(4)
print(index)  # Output: 4

# Check if an element is in the list
is_present = 5 in num_list
print(is_present)  # Output: True

num_list = [3, 1, 4, 1, 5, 9, 2]

# Sort the list in ascending order
num_list.sort()

# Reverse the order of elements
num_list.reverse()

print(num_list)  # Output: [9, 5, 4, 3, 2, 1, 1]

length = len(num_list)
print(length)  # Output: 7

