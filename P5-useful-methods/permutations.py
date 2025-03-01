from itertools import permutations

# Example list
data = [1, 2, 3]

# Generate all permutations
perm = permutations(data)

# Convert to a list and print
print(list(perm))
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]