# Write a Python script to concatenate the following dictionaries to create a new one

def concat_dicts_using_update(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

def concat_dicts_using_unpacking(*dicts):
    return {k: v for d in dicts for k, v in d.items()}

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

concatenated_dict_update = concat_dicts_using_update(dict1, dict2, dict3)

concatenated_dict_unpacking = concat_dicts_using_unpacking(dict1, dict2, dict3)

print("Concatenated dictionary (using update()):")
print(concatenated_dict_update)

print("\nConcatenated dictionary (using dictionary unpacking):")
print(concatenated_dict_unpacking)
