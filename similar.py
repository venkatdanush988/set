'''

5) Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.

'''

# Read the first set of values and convert to a set of integers
set1 = set(map(int, input().split()))

# Read the second set of values and convert to a set of integers
set2 = set(map(int, input().split()))

# Find the common values in both sets
common_values = set1.intersection(set2)

# Convert the common values to a sorted list
sorted_common = sorted(common_values)

# Print the common values with space separation, including a trailing space
print(" ".join(map(str, sorted_common)) + " ")
