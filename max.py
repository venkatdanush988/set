'''

7) Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1

'''

# Read input as a single line and split by spaces
input_values = input().split()

# Convert to a set of integers
values_set = set(map(int, input_values))

# Find the maximum and minimum values
max_value = max(values_set)
min_value = min(values_set)

# Print the results
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
