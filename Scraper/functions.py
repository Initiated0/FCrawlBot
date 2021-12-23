import os

def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# create_directory("Wiki")

def create_new_file(path):
    f = open(path,'w')
    f.write("")
    f.close()

# create_new_file("./test.txt")

def write_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

# write_to_file("Wiki/test.txt", "why this scraping will be such a drag.")

def clear_file(path):
    f = open(path,'w')
    f.close()

# clear_file("Wiki/test.txt")

def does_file_exists(path):
    return os.path.isfile(path)

# print(does_file_exists("Wiki/test2.txt"))

def read_data(path):
    with open(path, 'rt') as file:
        for line in file:
            print(line.replace("\n", ""))


read_data("Wiki/test.txt")
clear_file("Wiki/test.txt")

# now we will be scraping from "lazyfruits.com"