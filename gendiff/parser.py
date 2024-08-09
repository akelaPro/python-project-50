import json

import yaml


def parse(path):
    with open(path) as file:
        content = file.read()
        if content.endswith('yaml') or content.endswith('yml'):
            return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
        elif content.endswith('json'):
            return json.load(open(path, 'r'))
        raise ValueError('unsupported file format')
