import json

import yaml


def parse(path):
    if path.endswith('yaml') or path.endswith('yml'):
        return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
    elif path.endswith('json'):
        return json.load(open(path, 'r'))
    raise ValueError('unsupported file format')
