def plain_formatter(diff, path=""):
    result = ""
    for unit_diff in diff:
        status = unit_diff['status']
        name = path + unit_diff['name']
        if status == 'added':
            result += f"Property '{name}' was added with value: {to_str(unit_diff['what_added'])}\n"

        elif status == 'deleted':
            result += f"Property '{name}' was removed\n"

        elif status == 'changed':
            result += f"Property '{name}' was updated. From {to_str(unit_diff['from_first_dict'])} to {to_str(unit_diff['from_second_dict'])}\n"

        else:
            nested = plain_formatter(unit_diff.get('children', []), name + ".")
            result += nested
    return result


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
