import subprocess
import os
import sys
import textwrap

from progression_builder import get_progression
from voice_leading_builder import get_voice_leading

global_data = {
    "key": "c",
    "time_signature": "4/4"
}

chord_mapping = {
    "I": [0, 4, 7, 11], 
    "viidim/iii": [3, 6, 9, 12], 
    "V/iii": [11, 15, 18, 21], 
    "viidim/vi": [8, 11, 14, 17], 
    "V/vi": [4, 8, 11, 14], 
    "viidim/ii": [1, 4, 7, 10], 
    "V/ii": [9, 13, 16, 19], 
    "viidim/V": [6, 9, 12, 15], 
    "V/V": [2, 6, 9, 12], 
    "viidim/IV": [4, 7, 10, 13], 
    "V/IV": [0, 4, 7, 10], 
    "iii": [4, 7, 11, 14], 
    "vi": [9, 12, 16, 19], 
    "IV": [5, 9, 12, 16], 
    "ii": [2, 5, 12, 16], 
    "viidim": [11, 14, 17, 22], 
    "V6/4": [7, 12, 16, 19], 
    "N6": [5, 8, 13, 17], 
    "+6": [8, 12, 14, 18], 
    "V": [7, 11, 14, 17],
    "viidim/VII": [9, 12, 15, 18],
    "V/VII": [5, 9, 12, 15],
    "viidim/III": [2, 5, 8, 11],
    "V/III": [10, 14, 17, 20],
    "iv": [5, 8, 12, 15],
    "VII": [10, 14, 17, 20],
    "III": [3, 7, 10, 14],
    "VI": [8, 12, 15, 19],
    "iidim": [2, 5, 8, 11],
    "i": [0, 3, 7, 10]
}

# TODO
def get_chord_notes(key: str, chord: str) -> list:
    return []

def get_lilypond_notation(notes: list):
   # map user input to LilyPond syntax
   note_mapping = {
       'C': 'c', 'C#': 'cis', 'Db': 'des',
        'D': 'd', 'D#': 'dis', 'Eb': 'ees',
        'E': 'e', 'F': 'f', 'F#': 'fis',
        'Gb': 'ges', 'G': 'g', 'G#': 'gis',
        'Ab': 'aes', 'A': 'a', 'A#': 'ais',
        'Bb': 'bes', 'B': 'b'
   }

   return [note_mapping[note] for note in notes]

def shift_notes(notes: list, shift: int) -> str:
    # Define the note mapping
    note_to_num = {
        'c': 0, 'cis': 1, 'des': 1,
        'd': 2, 'dis': 3, 'ees': 3,
        'e': 4, 'f': 5, 'fis': 6,
        'ges': 6, 'g': 7, 'gis': 8,
        'aes': 8, 'a': 9, 'ais': 10,
        'bes': 10, 'b': 11
    }
    # Create a reverse mapping
    num_to_note = {v: k for k, v in note_to_num.items()}
  
    # Shift each note and join them back into a string
    shifted_notes = [num_to_note[(note_to_num[note] + shift) % 12] for note in notes]
    
    return shifted_notes

def generate_notation(filename, notes):
    with open(filename, 'w') as file:
        # Global settings

        global_string = textwrap.dedent(f'''\
            global = {{
              \\key {global_data["key"]} \\major
              \\time {global_data["time_signature"]}
            }}\n\n''')

        file.write(global_string)

        num_measures = 2

        file.write("\\parallelMusic voiceA,voiceB,voiceC,voiceD {\n")
        for i in range(num_measures):
            file.write(textwrap.dedent(f'''\
                {notes[0][i*4]}4 {notes[0][i*4 + 1]} {notes[0][i*4 + 2]} {notes[0][i*4 + 3]} |
                {notes[1][i*4]}4 {notes[1][i*4 + 1]} {notes[1][i*4 + 2]} {notes[1][i*4 + 3]} |
                {notes[2][i*4]}4 {notes[2][i*4 + 1]} {notes[2][i*4 + 2]} {notes[2][i*4 + 3]} |
                {notes[3][i*4]}4 {notes[3][i*4 + 1]} {notes[3][i*4 + 2]} {notes[3][i*4 + 3]} |
                '''))
        file.write("}\n\n")

        file.write('''\\score {
          \\new PianoStaff <<
             \\new Staff {
               \\global
               <<
                 \\relative c'' \\voiceA
                 \\\\
                 \\relative c'  \\voiceB
               >>
             }
             \\new Staff {
               \\global \\clef bass
               <<
                 \\relative c \\voiceC
                 \\\\
                 \\relative c \\voiceD
               >>
             }
          >>
        }
        ''')


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
    # bassline = input("Enter musical notes separated by space: ")

    # b = get_lilypond_notation(bassline.split())
    # t = shift_notes(b, 4)
    # a = shift_notes(b, 7)
    # s = shift_notes(b, 11)
    # notes = [s, a, t, b]

    progression, key = get_progression
    notes = get_voice_leading(progression, key)
    generate_notation('notes.ly', notes)
    open_pdf('notes.pdf')
