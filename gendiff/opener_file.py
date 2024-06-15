import json

import yaml 


def open_file(path):
    if path.endswith('yaml') or path.endswitch('yml'):
        return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
    else:
        return json.load(open(path, 'r'))
