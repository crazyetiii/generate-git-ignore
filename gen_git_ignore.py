import os
import sys

GIT_IGNORE_FILE_NAME = '.gitignore'
VERSION = 'v1.0'


def get_version():
    return 'generate .gitignore file('+VERSION+')'


def gen_svn_dir_str():
    return "# svn\n.svn\n\n"


def gen_visul_studio():
    return "# visual studio\nDebug\nRelease\n\n"


def write_2_file_path(git_ignore_path):
    print(f'current .gitignore file path:[{git_ignore_path}]')
    with open(git_ignore_path, 'w', encoding='utf-8', errors='ignore') as fw:
        fw.write(gen_svn_dir_str())
        fw.write(gen_visul_studio())


def get_end_str():
    return 'generate end!'


if __name__ == '__main__':
    print(get_version())
    write_2_file_path(os.getcwd()+"\\"+GIT_IGNORE_FILE_NAME)
    print(get_end_str())
