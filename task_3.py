def list_to_dict(elements: list) -> dict:
    result = {}
    for index, elem in enumerate(elements, start=1):
        result[f"k{index}"] = elem
    return result


a = [[1, 2, 3], [4, 5, 6]]

result = []
for list_ in a:
    result.append(
        list_to_dict(list_)
    )

print(result)
