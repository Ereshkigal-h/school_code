def print_reverse_keys(dictionary):
    for key in sorted(dictionary.keys(),reverse=True):
        print(f"{key} {dictionary[key]}")
