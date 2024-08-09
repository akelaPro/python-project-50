def generate_diff_tree(data1, data2):
    result = []
    keys1, keys2 = data1.keys(), data2.keys()
    all_keys = keys1 | keys2
    step_ressult = {}
    for key in sorted(all_keys):
        if key not in keys1:
            step_ressult = {
                'name': key,
                'status': 'added',
                'what_added': data2.get(key)
            }
            result.append(step_ressult)
        elif key not in keys2:
            step_ressult = {
                'name': key,
                'status': 'deleted',
                'what_deleted': data1.get(key)
            }
            result.append(step_ressult)
        elif data1.get(key) == data2.get(key):
            step_ressult = {
                'name': key,
                'status': 'unchangent',
                'intact': data1.get(key)
            }
            result.append(step_ressult)
        elif isinstance(
            data1.get(key), dict) and isinstance(
                data2.get(key), dict):
            step_ressult = {
                'name': key,
                'status': 'nested',
                'children': generate_diff_tree(
                    data1.get(key), data2.get(key))
            }
            result.append(step_ressult)
        else:
            step_ressult = {
                'name': key,
                'status': 'changed',
                'from_first_dict': data1.get(key),
                'from_second_dict': data2.get(key)
            }
            result.append(step_ressult)
    diff = sorted(result, key=lambda x: x['name'])
    return diff
