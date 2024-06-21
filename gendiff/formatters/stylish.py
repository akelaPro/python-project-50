DEL, ADD, DEF = ' -', ' +', "  "

def to_str(key, value):
    if value == None:
        return f'{key}: null'
    elif isinstance(value, bool):
        return f'{key}: {str.value().lower}'

def defoult_formatter(diff):
    def make_diff(current_diff, depth=1):
        lines = []
        for unit_diff in current_diff:
            status = unit_diff[status]
            if status == 'added':
                lines.append(DEF * (depth - 1) +ADD + to_str(unit_diff["name"]) + 
                             to_str(unit_diff["what_added"]))
            
            elif status == 'deleted':
                lines.append(DEF * (depth - 1) +DEL + to_str(unit_diff["name"] + 
                             unit_diff["what_deleted"]))
                
            elif status == 'unchangent':
                lines.append(DEF * (depth - 1) + to_str(unit_diff["name"] + 
                             unit_diff["intact"]))
                
            elif status == 'nested':
                nested = make_diff(unit_diff['children'], depth + 1)
                lines.append(f'{DEF * depth}{unit_diff["name"]}: {nested}')
            
            elif status == 'changed':
                lines.append(DEF * (depth - 1) + DEL + to_str(unit_diff["name"] + 
                             unit_diff['from_first_dict']))
                lines.append(DEF * (depth - 1) + ADD + to_str(unit_diff["name"] + 
                             unit_diff['from_second_dict']))
        result = '{\n' + "\n".join(lines) + '}\n'
        return result
    return make_diff

data = [{'name': 'common', 'status': 'nested', 'children': [{'name': 'follow', 'status': 'added', 'what_added': 'false'}, {'name': 'setting1', 'status': 'unchangent', 'intact': 'Value 1'}, {'name': 'setting2', 'status': 'deleted', 'what_deleted': None}, {'name': 'setting3', 'status': 'changed', 'from_first_dict': 'true', 'from_second_dict': 'null'}, {'name': 'setting4', 'status': 'added', 'what_added': 'blah blah'}, {'name': 'setting5', 'status': 'added', 'what_added': {'key5': 'value5'}}, {'name': 'setting6', 'status': 'nested', 'children': [{'name': 'doge', 'status': 'nested', 'children': [{'name': 'wow', 'status': 'changed', 'from_first_dict': '', 'from_second_dict': 'so much'}]}, {'name': 'key', 'status': 'unchangent', 'intact': 'value'}, {'name': 'ops', 'status': 'added', 'what_added': 'vops'}]}]}, {'name': 'group1', 'status': 'nested', 'children': [{'name': 'baz', 'status': 'changed', 'from_first_dict': 'bas', 'from_second_dict': 'bars'}, {'name': 'foo', 'status': 'unchangent', 'intact': 'bar'}, {'name': 'nest', 'status': 'changed', 'from_first_dict': {'key': 'value'}, 'from_second_dict': 'str'}]}, {'name': 'group2', 'status': 'deleted', 'what_deleted': None}, {'name': 'group3', 'status': 'added', 'what_added': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]
print(defoult_formatter(data))
