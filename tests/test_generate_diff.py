import pytest 

from gendiff.diff_builder import generate_diff

path1 = 'tests/fixtures/file1.json'
path2 = 'tests/fixtures/file2.json'
diff_file = 'tests/fixtures/result.txt'

def test_generate_diff():
    assert generate_diff(path1, path2) == open(diff_file).read()