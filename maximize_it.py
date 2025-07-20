from itertools import product

k, M = map(int, input().split())  # read number of lists and M
lists = []

for _ in range(k):
    data = list(map(int, input().split()))
    lists.append(data[1:])  # ignore the first number (length), only store list

# Try all combinations: one element from each list
all_combinations = product(*lists)

# For each combination, compute sum of squares % M
max_value = 0
for combo in all_combinations:
    total = sum(x**2 for x in combo) % M
    if total > max_value:
        max_value = total

print(max_value)
