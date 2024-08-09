DEL, ADD, DEF = '  - ', '  + ', "    "


def to_str(key, value, depth):
    if value is None:
        return f'{key}: null'
    elif isinstance(value, bool):
        return f'{key}: {str(value).lower()}'
    elif isinstance(value, dict):
        return format_dict(key, value, depth)
    else:
        return f'{key}: {str(value)}'


def format_dict(key, value, depth):
    lines = [f'{key}: {{']
    for item in value.items():
        lines.append(
            DEF * (depth + 1) + to_str(item[0], item[1], depth + 1))
    lines.append(DEF * depth + '}')
    return '\n'.join(lines)


def format_diff_unit(unit_diff, depth):
    status = unit_diff['status']
    indent_del = DEF * (depth - 1)
    indent_add = DEF * depth
    name = unit_diff['name']
    if status == 'added':
        return (f'{indent_del}{ADD}'
                f'{to_str(name, unit_diff["what_added"], depth)}')
    elif status == 'deleted':
        return (f'{indent_del}{DEL}'
                f'{to_str(name, unit_diff["what_deleted"], depth)}')
    elif status == 'unchangent':
        return (f'{indent_add}'
                f'{to_str(name, unit_diff["intact"], depth)}')
    elif status == 'nested':
        return (f'{indent_add}{name}: '
                f'{make_diff(unit_diff["children"], depth + 1)}')
    elif status == 'changed':
        return (f'{indent_del}{DEL}'
                f'{to_str(name, unit_diff["from_first_dict"], depth)}\n'
                f'{indent_del}{ADD}'
                f'{to_str(name, unit_diff["from_second_dict"], depth)}')


def make_diff(current_diff, depth=1):
    lines = [format_diff_unit(unit_diff, depth) for unit_diff in current_diff]
    output = '{\n' + '\n'.join(filter(None, lines)) + f'\n{DEF * (depth - 1)}}}'
    return output


def default_formatter(diff):
    return make_diff(diff)
