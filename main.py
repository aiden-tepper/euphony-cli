import subprocess
import os
import sys
import lilypond

from progression_builder import get_progression
from voice_leading.voice_leading_builder import get_voice_leading
from sheet_music.lilypond_builder import generate_notation
from play_prog import *

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

    generate_notation('sheet_music/notes.ly', chords, key, major_minor)
    subprocess.run([lilypond.executable(), '--output=./sheet_music/notes', 'sheet_music/notes.ly'])
    open_pdf('sheet_music/notes.pdf')
    
    play_organ(chords)
