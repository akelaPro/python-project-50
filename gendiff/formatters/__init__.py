from gendiff.formatters.stylish import default_formatter
from gendiff.formatters.plain import plain_formatter

def diff_formaters(diff, format):
    if format == 'stylish':
        return default_formatter(diff)
    elif format == 'plain':
        return plain_formatter(diff)