import json


def generate_diff(file_path1, file_path2):

    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    diff = []

    for key in sorted(data1.keys() | data2.keys()):
        if key not in data2:
            diff.append(f'- {key}: {str(data1[key])}')
        elif key not in data1:
            diff.append(f'+ {key}: {data2[key]}')
        elif key in data1 and data2 and data1[key] != data2[key]:
            diff.append(f'- {key}: {data1[key]}')
            diff.append(f'+ {key}: {data2[key]}')
        else:
            diff.append(f'  {key}: {data2[key]}')

    stail_diff = "\n ".join(diff)

    return f'{{\n {stail_diff}\n}}'
