'''

SET
1) Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
Note: There is trailing space at the end of output

'''

# Read the number of inputs
n = int(input())

# Initialize an empty set
values_set = set()

# Read n values from input
for _ in range(n):
    value = int(input())
    values_set.add(value)

# Convert the set to a sorted list
sorted_values = sorted(values_set)

# Print the sorted values with space separation, including a trailing space
print(" ".join(map(str, sorted_values)) + " ")
