import pytest

from gendiff.diff_builder import generate_diff

@pytest.mark.parametrize("file_path_1, file_path_2, result_file_path", [
    ('tests/fixtures/file1.json',
    'tests/fixtures/file2.json', 'tests/fixtures/result.txt')])


def test_generate_diff():
    assert generate_diff(file_path1, file_path2) == result_file_path