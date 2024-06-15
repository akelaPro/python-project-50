def generate_diff_tree(file1, file2):
    result = []
    keys1, keys2 = file1.keys(), file2.keys()
    all_keys = keys1 | keys2
    for key in all_keys:
        if key not in keys1:
            step_res = {
                'name': key,
                'status': 'added',
                'what_added': file2.get(key)
            }
            result.append(step_res)
        elif key not in keys2:
            step_res = {
                'name': key,
                'status': 'deleted',
                'what_deleted': file1.get(key)
            }
            result.append(step_res)
        elif file1.get(key) == file2.get(key):
            step_res = {
                'name': key,
                'status': 'unchagent',
                'intact': file1.get(key)
            }
            result.append(step_res)
        elif isinstance(
            file1.get(key), dict) and isinstance(
                file2.get(key), dict):
            step_res = {
                'name': key,
                'status': 'nested',
                'children': generate_diff_tree(
                    file1.get(key), file2.get(key))
            }
            result.append(step_res)
        else:
            step_result = {
                'name': key,
                'status': 'changed',
                'from_first_dict': file1.get(key),
                'from_second_dict': file2.get(key)
            }
            result.append(step_res)
    diff = sorted(result, key=lambda x: x['name'])
    return diff