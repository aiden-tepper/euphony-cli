import subprocess
import os
import sys

def get_lilypond_notation(notes):
    # map user input to LilyPond syntax
    note_mapping = {
        "A": "a",
        "B": "b",
        "C": "c",
        "D": "d",
        # add more notes as needed
    }

    return " ".join(note_mapping[note.upper()] for note in notes.split())

def generate_notation(filename):
    # call LilyPond command-line tool on the file
    subprocess.call(['lilypond', filename])

def open_pdf(filename):
    # open the generated PDF file
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filename))
    elif os.name == 'nt':
        os.startfile(filename)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filename))

if __name__ == "__main__":
    notes = input("Enter musical notes separated by space: ")
    lilypond_notation = get_lilypond_notation(notes)

    with open('notes.ly', 'w') as file:
        file.write('\\relative c\' { ' + lilypond_notation + ' }')

    generate_notation('notes.ly')
    open_pdf('notes.pdf')
