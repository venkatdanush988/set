'''

6)
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5

'''

# Read input as a single line and split by spaces
input_values = input().split()

# Convert to a set to get unique values
unique_values_set = set(map(int, input_values))

# Get the number of unique elements
number_of_elements = len(unique_values_set)

# Print the number of unique elements
print(number_of_elements)
