from gendiff.diff_tree import generate_diff_tree


from gendiff.opener_file import open_file


from gendiff.formatters.__init__ import diff_formaters


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = open_file(file_path1)
    file2 = open_file(file_path2)
    diff = generate_diff_tree(file1, file2)
    return diff_formaters(diff, format)
