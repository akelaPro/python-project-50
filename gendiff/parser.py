import json

import yaml

import os


def parse(path):
    with open(path) as file:
        content = file.read()
        _, extension = os.path.splitext(path)
        extension = extension.lower()
        if extension in ['.yaml', '.yml']:
            return yaml.safe_load(content)
        elif extension == '.json':
            return json.loads(content)
        else:
            raise ValueError('unsupported file format')
