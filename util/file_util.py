#import os
import re
from tabnanny import check

#parameter for file name format
#file extension type

class FileUtil():

    #return a list of file names that start with given prefix
    def filter_files_by_prefix(self, file_list, prefix):
        return list(filter(lambda x: (x.startswith(prefix)), file_list))

    def check_for_trailing_digits(file):
        return re.search(r'\d+$', file)

    def remove_trailing_digits(file):
        cleaned_file = re.sub(r'\d+$', '', file)
        return cleaned_file

    if __name__ == "__main__":

        print(str(check_for_trailing_digits("hello")))
        print(str(check_for_trailing_digits("hello1234")))

        print(str(remove_trailing_digits("hello")))
        print(str(remove_trailing_digits("hello1234")))


        # list = ['the', 'quick1', 'brown23', 'fox456']
        # regex = "r'\d+$'"
        # removed_suffix = remove_suffix(list, regex)
        # print(str(removed_suffix))

#     test = FileFilter(["the", "their", "this"], "th")
#     filtered = test.filter_files()
#     print(str(filtered))
