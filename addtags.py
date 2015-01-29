#! /usr/bin/python3

import os
import argparse
import json

tags = { '.txt': 'TEXT', '.py': 'PYTHON', '.jpg': 'PHOTO', '.png': 'PHOTO',
         '.c': 'C', '.cpp': 'C++', '.avi': 'MEDIA', '.mkv': 'MEDIA', 
         '.html': 'HTML', '.css': 'CSS', '.js': 'JAVASCRIPT', '.class': 'JAVA',
         '.java': 'JAVA', '.apk': 'ANDROID', '.exe': 'WINDOWS EXECUTABLE', 
         '.doc': 'WORD DOCUMENT', '.docx': 'WORD DOCUMENT', 
         '.ppt': 'PRESENTATION', '.pdf': 'PDF', '.asp': 'ASP', 
         '.pptx': 'PRESENTATION', '.gz': 'COMPRESSED', '.aspx': 'ASP',
         '.htm': 'HTML', '.jsp': 'JAVA SERVER PAGES', '.mov': 'MEDIA',
         '.fnt': 'FONT', '.amr': 'VOICE RECORDING', '.mp3': 'AUDIO',
         '.flv': 'VIDEO', '.mp4': 'VIDEO', '.xml': 'EXTENSIBLE MARKUP',
         '.obj': 'OBJECT', '.rar': 'COMPRESS', '.zip': 'COMPRESS',
         '.gif': 'PHOTO', '.iso': 'SYSTEM IMAGE', '.svg': 'PHOTO',
         '.bin': 'BINARY', '.cfg': 'CONFIGURATION', '.sh': 'SHELL SCRIPT',
         '.tar': 'ARCHIVE', '.json': 'JSON', 'none': 'NONE' }

indexed = {}

def get_tag(ext):
    if ext not in tags.keys():
        return 'NONE'
    else:
        return tags[ext]

def add_tag(files):
    path, ext = os.path.splitext(files)
    filename = os.path.basename(files)
    path = os.path.abspath(files)
    for extension, tag in tags.items():
        indexed.setdefault(tag, [])
    tag = get_tag(ext)
    indexed[tag].append((filename, path))

def traverse(directory):
    for root, dirs, files in os.walk(directory):
        for each_file in files:
            add_tag(each_file)

def dumpJson():
    with open('tags.json', 'w') as json_tags:
        json_tags.write(json.dumps(indexed, sort_keys = True, indent = 4))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Index & alot tags to\
                                                    files.')
    parser.add_argument('-d', '--directory', action = 'store', 
                         dest="directory", 
                         help = "Recursively traverse given directory and\
                                 alot tags.")
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        directory = '/home'
    traverse(directory)
    dumpJson()
    print("Indexed Success! Now displaying tagged files...")
    for tag, files in indexed.items():
        if files:
            print("Tag: " + tag + " has files: ")
            for each_file, path in files:
                print("File: " + each_file + " with path: " + path)
