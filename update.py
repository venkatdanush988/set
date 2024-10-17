'''
8) Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5

'''
# Read the first set of values and convert to a set of integers
set1 = set(map(int, input().split()))

# Read the second set of values and convert to a set of integers
set2 = set(map(int, input().split()))

# Update set1 with values from set2
set1.update(set2)

# Convert the updated set to a sorted list
sorted_combined = sorted(set1)

# Print the updated values with space separation
print(" ".join(map(str, sorted_combined)))
