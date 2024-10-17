'''

4) Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.


'''

# Read the set of values and convert to a set of integers
values_set = set(map(int, input().split()))

# Read the element to be deleted
element_to_delete = int(input())

# Check if the element is in the set
if element_to_delete in values_set:
    # Remove the element
    values_set.remove(element_to_delete)
    # Convert the set to a sorted list
    sorted_values = sorted(values_set)
    # Print the remaining values with space separation, including a trailing space
    print(" ".join(map(str, sorted_values)) + " ")
else:
    # Print the message if the element is not found
    print("Given value is not present in the set list.")
