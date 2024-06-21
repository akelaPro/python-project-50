import pytest 

from gendiff.diff_builder import generate_diff

path1_json = 'tests/fixtures/file1.json'
path2_json = 'tests/fixtures/file2.json'
diff_file = 'tests/fixtures/result.txt'
path1_yaml = 'tests/fixtures/file1.yaml'
path2_yaml = 'tests/fixtures/file2.yaml'
path_nested1_json = 'tests/fixtures/nested1.json'
path_nested2_json = 'tests/fixtures/nested2.json'
pat_nested_result = 'tests/fixtures/nested_result.txt'
@pytest.mark.parametrize('path1, path2, diff',
                          [(path1_json, path2_json, diff_file),
                            (path1_yaml, path2_yaml, diff_file),
                            (path_nested1_json, path_nested2_json,
                             pat_nested_result)])
def test_generate_diff(path1, path2, diff):
    assert generate_diff(path1, path2) == open(diff).read()
