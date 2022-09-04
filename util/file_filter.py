#import os

#parameter for file name format
#file extension type

class FileFilter(object):
    def __init__(self, file_list, prefix):
        self.file_list = file_list
        self.prefix = prefix 

    #return a list of file names that start with given prefix
    def filter_files(self):
        my_files = self.file_list
        result = list(filter(lambda x: (x.startswith(self.prefix)), my_files))
        return result
        

if __name__ == "__main__":

    test = FileFilter(["the", "their", "this"], "th")
    filtered = test.filter_files()
    print(str(filtered))
