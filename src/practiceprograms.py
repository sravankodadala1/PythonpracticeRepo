
# Program to find the sum of elements in a list
# Sample list
numbers = [1, 2, 3, 4, 5]
# Calculate the sum using the built-in sum() function
list_sum = sum(numbers)
# Print the result
print("Sum of elements:", list_sum)


#Program to Square Each Element in a List:

# Sample list
numbers = [1, 2, 3, 4, 5]
# Square each element without using list comprehension
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
# Print the squared elements
print("Squared elements:", squared_numbers)



Program to filter even numbers from a list without using list comprehension
# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Filter even numbers without using list comprehension
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
# Print the result
print("Even numbers:", even_numbers)


# Program to find the maximum element in a list without using built-in max()
# Sample list
numbers = [1, 7, 3, 9, 5]
# Find the maximum element without using built-in max()
max_element = numbers[0]
for num in numbers[1:]:
    if num > max_element:
        max_element = num
# Print the result
print("Maximum element:", max_element)

# Program to reverse a list without using the built-in reverse()
# Sample list
fruits = ["apple", "banana", "orange", "grape"]
# Reverse the list without using built-in reverse()
reversed_list = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_list.append(fruits[i])
# Print the reversed list
print("Reversed list:", reversed_list)



#Program to find the union of two sets without using built-in union()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Find the union without using built-in union()
union_set = set1.copy()
for element in set2:
    if element not in union_set:
        union_set.add(element)
# Print the result
print("Union of sets:", union_set)


# Program to remove duplicate elements from a list and convert to a set without using built-in set()

# Sample list
numbers = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates and convert to set without using built-in set()
unique_set = set()
for num in numbers:
    unique_set.add(num)
# Print the result
print("Set with unique elements:", unique_set)


# Program to perform set difference operation without using built-in difference()

# Sample sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Perform set difference without using built-in difference()
difference_set = set1.copy()
for element in set2:
    if element in difference_set:
        difference_set.remove(element)
# Print the result
print("Set difference:", difference_set)


# Calculate the sum of numbers in a list without using built-in sum function
def calculate_sum(numbers):
    result = 0
    # Iterate through each number in the list
    for num in numbers:
        # Add the current number to the result
        result = result + num
    return result
# Example usage
numbers_list = [1, 2, 3, 4, 5]
sum_result = calculate_sum(numbers_list)
print("Sum of the numbers:", sum_result)



# Find the maximum number in a list without using built-in max function
def find_max(numbers):
    # Assume the first number is the maximum
    maximum = numbers[0]
    # Iterate through each number in the list
    for num in numbers:
        # Update the maximum if a larger number is found
        if num > maximum:
            maximum = num
    return maximum
# Example usage
numbers_list = [5, 8, 2, 10, 3]
max_result = find_max(numbers_list)
print("Maximum number:", max_result)


# Check if a number is prime without using built-in functions
def is_prime(number):
    # 0 and 1 are not prime numbers
    if number < 2:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        # If a factor is found, the number is not prime
        if number % i == 0:
            return False
    return True
# Example usage
num_to_check = 17
if is_prime(num_to_check):
    print(num_to_check, "is a prime number.")
else:
    print(num_to_check, "is not a prime number.")


















