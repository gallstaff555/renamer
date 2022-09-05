#import os
import re
from tabnanny import check

#parameter for file name format
#file extension type

class FileUtil():

    #return a list of file names that start with given prefix
    def filter_files(file_list, prefix):
        return list(filter(lambda x: (x.startswith(prefix)), file_list))
    

    def remove_trailing_digits(file_list, check, clean):
        for i in range(len(file_list)):
            if check(file_list[i]) is not None:
                file_list[i] = clean(file_list[i])


    def check_for_trailing_digits(file):
        return re.search(r'\d+$', file)

    def remove_trailing_digits(file):
        cleaned_file = re.sub(r'\d+$', '', file)
        return file
    # def remove_suffix(file_list, suffix):
    #     #return list(filter(lambda x: (x.endswith(postfix)), file_list))
    #     #return list(filter(lambda x: postfix), file_list)
    #     for file in file_list:
    #         print(suffix)
    #         if re.search(suffix, file):
    #             print(suffix)
    #             #remove digits from end of filename
    #             end = -1
    #             while str(file[end]).isdigit():
    #                 end -= 1
    #             file = file[:(end+1)]
    #             print(file)
    #     return file_list

    if __name__ == "__main__":

        print(str(check_for_trailing_digits("hello")))
        print(str(check_for_trailing_digits("hello1234")))

        print(str(remove_trailing_digits("hello")))
        print(str(remove_trailing_digits("hello1234")))

        print

        # list = ['the', 'quick1', 'brown23', 'fox456']
        # regex = "r'\d+$'"
        # removed_suffix = remove_suffix(list, regex)
        # print(str(removed_suffix))

#     test = FileFilter(["the", "their", "this"], "th")
#     filtered = test.filter_files()
#     print(str(filtered))
