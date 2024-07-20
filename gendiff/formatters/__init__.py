from gendiff.formatters.stylish import default_formatter
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import json_format

def diff_formaters(diff, format):
    if format == 'stylish':
        return default_formatter(diff)
    elif format == 'plain':
        return plain_formatter(diff)
    elif format == 'json':
        return json_format(diff)