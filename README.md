# TagLask
A light weight webapp made on Flask to index and search user files. It contains three files:

- addtags.py
- findmyfiles.py
- webapp.py

`addtags.py` and `findmyfiles.py` can be used as a command line application too, seperately, without using the webapp.py

### Addtags.py
Use this script to traverse a directory and add tags to it. It can be used as a command line application as following:

`python addtags.py -h` to ask for help and you'll get the following:

```
usage: addtags.py [-h] [-d DIRECTORY]

Index & alot tags to files.

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Recursively traverse given directory and alot tags.
```

To traverse a directory run addtags.py as following:

`python addtags.py -d /home/`

or

`python addtags.py --directory /home/`

This would index all the files under `/home/` directory.

Now you can run `findmyfiles.py` to search for the files.

### FindMyFiles.py

Use this script to find the files under the directory already traversed by `addtags.py`. It can be used as a command 
line application as the following:

`python findmyfiles.py -h` to ask for help and you'll get the following:

```
usage: findmyfiles.py [-h] [-f FILE] [-t TAG]

Find your files.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  give filename/pattern to match files.
  -t TAG, --tag TAG     give the tag
```

It is optional to give filename but **tag** is essential. This application wouldn't work without *tag*.
Here `tag` can be anything from pre-defined list (given at the end).

You can run findmyfiles as following:

`python findmyfiles -t "WORD DOCUMENT"`

**OPTIONALLY, you can provide a filename too.**

### Webapp.py

You can simply run a webapp to traverse, index & search files.

Go to `/add` to add the files.

Go to `/search` to search the files.

#### Tags currently the app has:

```
* 'TEXT' 
* 'PYTHON' 
* 'PHOTO' 
* 'C' 
* 'C++' 
* 'MEDIA' 
* 'HTML' 
* 'CSS' 
* 'JAVASCRIPT'
* 'JAVA' 
* 'ANDROID' 
* 'WINDOWS EXECUTABLE'
* 'WORD DOCUMENT' 
* 'PRESENTATION'
* 'PDF'
* 'COMPRESSED'
* 'ASP'
* 'JAVA SERVER PAGES'
* 'FONT'
* 'VOICE RECORDING'
* 'AUDIO'
* 'VIDEO'
* 'EXTENSIBLE MARKUP'
* 'OBJECT'
* 'COMPRESS'
* 'PHOTO'
* 'SYSTEM IMAGE'
* 'BINARY'
* 'CONFIGURATION'
* 'SHELL SCRIPT'
* 'ARCHIVE'
* 'JSON'
* 'NONE'
```
