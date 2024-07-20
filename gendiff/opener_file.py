import json

import yaml


def open_file(path):
    if path.endswith('yaml') or path.endswith('yml'):
        return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
    else:
        return json.load(open(path, 'r'))
