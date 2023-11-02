import subprocess
import os
import sys

from progression_builder import get_progression
from voice_leading_builder import get_voice_leading
from lilypond_builder import generate_notation

def open_pdf(filename):
    # open the generated PDF file
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filename))
    elif os.name == 'nt':
        os.startfile(filename)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filename))

if __name__ == "__main__":
    progression, key, major_minor = get_progression()
    chords = get_voice_leading(progression, key, major_minor)
    # print(chords)
    # chords = [[2, 5, 9, 12], [5, 7, 11, 14], [4, 7, 11, 12]]
    generate_notation('notes.ly', chords, key, major_minor)
    open_pdf('notes.pdf')
