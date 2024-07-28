import pytest

from gendiff.diff_builder import generate_diff

NESTED_FILE = {
  'nested1.json': 'tests/fixtures/nested1.json',
  'nested2.json': 'tests/fixtures/nested2.json',
  'nested1.yaml': 'tests/fixtures/nested1.yaml',
  'nested2.yaml': 'tests/fixtures/nested2.yaml'
}

PLAIN_FILE = {
'file1.json': 'tests/fixtures/file1.json',
'file2.json': 'tests/fixtures/file2.json',
'file1.yaml': 'tests/fixtures/file1.yaml',
'file2.yaml': 'tests/fixtures/file2.yaml'
}

RESULT = {
'plain_result': 'tests/fixtures/plain_result.txt',
'nested_result': 'tests/fixtures/nested_result.txt',
'defoult_result': 'tests/fixtures/result.txt',
'for_json_formatter': 'tests/fixtures/json_formatter_result.txt'
}


@pytest.mark.parametrize('path1, path2, formatter, diff',
  [(PLAIN_FILE['file1.json'], PLAIN_FILE['file2.json'], 'stylish', RESULT['defoult_result']),
  (PLAIN_FILE['file1.yaml'], PLAIN_FILE['file2.yaml'], 'stylish', RESULT['defoult_result']),
   (NESTED_FILE['nested1.json'], NESTED_FILE['nested2.json'], 'stylish', RESULT['nested_result']),
   (NESTED_FILE['nested1.yaml'], NESTED_FILE['nested2.yaml'], 'stylish', RESULT['nested_result']),
   (NESTED_FILE['nested1.json'], NESTED_FILE['nested2.json'], 'plain', RESULT['plain_result']),
   (NESTED_FILE['nested1.yaml'], NESTED_FILE['nested2.yaml'], 'plain', RESULT['plain_result']),
   (NESTED_FILE['nested1.json'], NESTED_FILE['nested2.json'], 'json', RESULT['for_json_formatter'])])
def test_generate_diff(path1, path2, formatter, diff):
  assert generate_diff(path1, path2, formatter) == open(diff).read()
