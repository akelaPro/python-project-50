def plain_formatter(diff, path=""):
    result = []
    for unit_diff in diff:
        status = unit_diff['status']
        name = path + unit_diff['name']
        if status == 'added':
            item = to_str(unit_diff['what_added'])
            result.append(f"Property '{name}' was added with value: {item}")

        elif status == 'deleted':
            result.append(f"Property '{name}' was removed")

        elif status == 'changed':
            old_item = to_str(unit_diff['from_first_dict'])
            new_item = to_str(unit_diff['from_second_dict'])
            result.append( f"Property '{name}' was updated. From {old_item} to {new_item}")

        else:
            nested = plain_formatter(unit_diff.get('children', []), name + ".")
            result.extend(nested.splitlines())

    return '\n'.join(result)  
    

    


def to_str(item):
    if isinstance(item, str):
        return f"'{str(item)}'"
    elif isinstance(item, dict):
        return '[complex value]'
    elif isinstance(item, bool):
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return str(item)
