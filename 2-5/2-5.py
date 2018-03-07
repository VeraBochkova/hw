import subprocess
import os


def create_directory_if_missing(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print('Directory {0} was created'.format(folder_path))


def convert_images(curr_dir, path, file_list):
    path_to_converter = os.path.join(curr_dir, 'convert.exe')
    path_to_result = os.path.join(curr_dir, 'Result')
    create_directory_if_missing(path_to_result)
    for file in file_list:
        subprocess.run(path_to_converter + ' "' + os.path.join(path, file) + '" -resize 200 "' + os.path.join(path_to_result, file) + '"')


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_source = os.path.join(current_dir, 'Source')
    files = os.listdir(path_to_source)
    convert_images(current_dir, path_to_source, files)

