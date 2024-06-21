DEL, ADD, DEF = ' -', ' +', "  "

def to_str(key, value):
    if value == None:
        return f'{key}: null'
    elif isinstance(value, bool):
        return f'{key}: {str(value).lower()}'  
    else:
        return f'{key}: {value}'

def default_formatter(diff):
    def make_diff(current_diff, depth=1):
        lines = []
        for unit_diff in current_diff:
            status = unit_diff['status']
            if status == 'added':
                lines.append(DEF * (depth - 1) + ADD + to_str(unit_diff["name"], unit_diff["what_added"]))
            
            elif status == 'deleted':
                lines.append(DEF * (depth - 1) + DEL + to_str(unit_diff["name"], unit_diff["what_deleted"]))
                
            elif status == 'unchanged':
                lines.append(DEF * (depth - 1) + to_str(unit_diff["name"], unit_diff["intact"]))
                
            elif status == 'nested':
                nested = make_diff(unit_diff['children'], depth + 1)
                lines.append(f'{DEF * depth}{unit_diff["name"]}: {nested}')
            
            elif status == 'changed':
                lines.append(DEF * (depth - 1) + DEL + to_str(unit_diff["name"], unit_diff['from_first_dict']))
                lines.append(DEF * (depth - 1) + ADD + to_str(unit_diff["name"], unit_diff['from_second_dict']))
        output = '{\n' + '\n'.join(lines) + '{\n'
        return output
    return make_diff(diff)

