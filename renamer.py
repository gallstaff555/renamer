import os
import argparse
from util.file_filter import FileFilter

def get_arguments():
    parser = argparse.ArgumentParser();
    parser.add_argument('--path', dest='path', metavar='-p', type=str, nargs=1, help="Path where files will be renamed.")

    args = parser.parse_args()
    return args

def get_files_in_dir(path):
    return os.listdir(path)

def get_target_dir(path):
    target_dir = str(path)[2:-2] #strip [' and ']
    if (target_dir[-1] != '/'):
        target_dir += '/'
    return target_dir

def rename_file(path, src, dst):
    os.rename(path + src, path + dst)

if __name__ == "__main__":

    args = get_arguments()
    target_dir = get_target_dir(args.path)

    print(f"Beginning file renaming in {target_dir}...")
    print(f"Files to be renamed: {get_files_in_dir(target_dir)}")

    rename_file(target_dir, 'test', 'test2')

    my_formatter = FileFilter()