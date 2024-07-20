DEL, ADD, DEF = '  - ', '  + ', "    "


def to_str(key, value, depth):
    if value is None:
        return f'{key}: null'
    elif type(value) is bool:
        return f'{key}: {str(value).lower()}'
    elif type(value) is dict:
        lines = [f'{key}: {{']
        for item in value.items():
            lines.append(
                DEF * (depth + 1) + to_str(
                    item[0], item[1], depth + 1))
        lines.append((DEF * (depth)) + '}')
        return '\n'.join(lines)
    else:
        return f'{key}: {str(value)}'


def default_formatter(diff):
    def make_diff(current_diff, depth=1):
        lines = []
        for unit_diff in current_diff:
            status = unit_diff['status']
            if status == 'added':
                lines.append(DEF * (depth - 1) + ADD + to_str(
                    unit_diff["name"], unit_diff["what_added"], depth))

            elif status == 'deleted':
                lines.append(DEF * (depth - 1) + DEL + to_str(
                    unit_diff["name"], unit_diff["what_deleted"], depth))

            elif status == 'unchangent':
                lines.append(DEF * (depth) + to_str(
                    unit_diff["name"], unit_diff["intact"], depth))
                
            elif status == 'nested':
                nested = make_diff(unit_diff['children'], depth + 1)
                lines.append(f'{DEF * depth}{unit_diff["name"]}: {nested}')

            elif status == 'changed':
                lines.append(DEF * (depth - 1) + DEL + to_str(
                    unit_diff["name"], unit_diff['from_first_dict'], depth))
                lines.append(DEF * (depth - 1) + ADD + to_str(
                    unit_diff["name"], unit_diff['from_second_dict'], depth))
        output = '{\n' + '\n'.join(lines) + f"\n{(DEF * (depth - 1))}}}"
        return output
    return make_diff(diff)
