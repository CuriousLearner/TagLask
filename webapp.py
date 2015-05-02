#! /usr/bin/python3

from flask import Flask, render_template, request, flash, session, redirect, url_for
import addtags
import os
import findmyfiles

app = Flask(__name__)
app.secret_key = 'aslkdfoiq'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        directory = request.form['directory']
	if os.path.exists(directory):
            addtags.traverse(directory)
            addtags.dumpJson()
            flash('All files in directory: ' + directory + ' indexed.')
            flash('Please go to <a href="search">search</a> to search for the files.')
        else:
            flash('Invalid directory path. Try again with a valid path.')
    return render_template('add.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = None
    if request.method == 'POST':
        filename = request.form['filename']
        file_type = request.form['file_type']
        findmyfiles.loadJson()
        results = findmyfiles.findmyfiles(filename, file_type)
        if not results:
            flash('No files found. Please try with a different query.')
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)