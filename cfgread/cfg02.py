#!/usr/bin/env python3

USER_FILE = input("Please enter the name of the file you would like to load: ")


## create file object in "r"ead mode
configfile = open(USER_FILE , "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## Function for line count of a file


def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1



## display list with no "\n"
print(configlist)

print("Number of lines in the file: ",file_lengthy(USER_FILE))


## Always close your file
configfile.close()

