#! /usr/bin/python3

import argparse
import json
from re import search
from sys import exit

indexed = {}
file_path = []

def loadJson():
    with open('tags.json', 'r') as json_data:
        global indexed
        indexed = json.load(json_data)

def findmyfiles(filename, tag):
    if tag in indexed.keys():
        for each_file in indexed[tag]:
            actualfile = each_file[0]
            path = each_file[1]
            if search(filename, actualfile):
                file_path.append([actualfile, path])
    return file_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find your files.')
    parser.add_argument('-f', '--file', action="store", dest="file",
                         help='give filename/pattern to match files.')
    parser.add_argument('-t', '--tag', action="store", dest="tag", 
                         help='give the tag')
    args = parser.parse_args()
    loadJson()
    if not args.tag:
        print('You need to provide the tag name. Exiting Now!')
        exit(1)
    elif not args.file:
        args.file = ''
    file_path = findmyfiles(args.file, args.tag)
    if not file_path:
        print("0 Matches found. Please try a different search!")
    else:
        for each_file in file_path:
            print('File: ' + each_file[0] + ' found at: ' + each_file[1])
