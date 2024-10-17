'''

9) Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''

# Read the number of values
n = int(input())

# Initialize an empty list to store input values
input_values = []

# Read n values from input
for _ in range(n):
    value = int(input())
    input_values.append(value)

# Count duplicates using a dictionary
value_count = {}
for value in input_values:
    if value in value_count:
        value_count[value] += 1
    else:
        value_count[value] = 1

# Calculate the number of duplicate values
duplicate_count = sum(count - 1 for count in value_count.values() if count > 1)

# Create a set of unique values
unique_values_set = set(input_values)

# Print the results
print(f"Duplicate Values: {duplicate_count}")
print(" ".join(map(str, sorted(unique_values_set))) + " ")
