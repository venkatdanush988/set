'''

2) Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
Note: There is no trailing space at the end of output.

'''

# Read input as a single line and split by spaces
input_values = input().split()

# Convert to a set of integers
values_set = set(map(int, input_values))

# Convert the set to a sorted list
sorted_values = sorted(values_set)

# Print the sorted values with space separation, no trailing space
print(" ".join(map(str, sorted_values)))
