def calculate_structure_sum(*params):
    total_sum = 0
    for i in params:
        if isinstance(i, (int, float)):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            total_sum += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            total_sum += calculate_structure_sum(*i.keys(), *i.values())

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)