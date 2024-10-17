'''

3) Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.

'''

# Read the first set of values and convert to a set of integers
set1 = set(map(int, input().split()))

# Read the second set of values and convert to a set of integers
set2 = set(map(int, input().split()))

# Find the different values in set1 (those not in set2)
difference = set1 - set2

# Convert to a sorted list
sorted_difference = sorted(difference)

# Print the different values with space separation, including a trailing space
print(" ".join(map(str, sorted_difference)) + " ")
