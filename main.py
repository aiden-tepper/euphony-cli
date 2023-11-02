import subprocess
import os
import sys
import textwrap

from progression_builder import get_progression
from voice_leading_builder import get_voice_leading

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

def to_note(note_num) -> str:
    num_to_note = {
        0: 'c', 1: 'cis', 1: 'des',
        2: 'd', 3: 'dis', 3: 'ees',
        4: 'e', 5: 'f', 6: 'fis',
        6: 'ges', 7: 'g', 8: 'gis',
        8: 'aes', 9: 'a', 10: 'ais',
        10: 'bes', 11: 'b'
    }

    return num_to_note[note_num % 12]

def generate_notation(filename, chords, key, major_minor):
    with open(filename, 'w') as file:
        # Global settings

        global_string = textwrap.dedent(f'''\
            global = {{
              \\key {key} \\{major_minor}
              \\time 4/4
            }}\n\n''')

        file.write(global_string)

        # chords = [[10, 13, 20, 24], [10, 15, 19, 25], [8, 15, 19, 24]]
        chords = list(zip(*chords))
        # chords = [[10, 10, 8], [13, 15, 15], [20, 19, 19], [24, 25, 24]]

        file.write("\\parallelMusic voiceA,voiceB,voiceC,voiceD {\n")
        # for i in range(len(chords[0])):
        #     # file.write(textwrap.dedent(f'''\
        #     #     {notes[0][i*4]}4 {notes[0][i*4 + 1]} {notes[0][i*4 + 2]} {notes[0][i*4 + 3]} |
        #     #     {notes[1][i*4]}4 {notes[1][i*4 + 1]} {notes[1][i*4 + 2]} {notes[1][i*4 + 3]} |
        #     #     {notes[2][i*4]}4 {notes[2][i*4 + 1]} {notes[2][i*4 + 2]} {notes[2][i*4 + 3]} |
        #     #     {notes[3][i*4]}4 {notes[3][i*4 + 1]} {notes[3][i*4 + 2]} {notes[3][i*4 + 3]} |
        #     #     '''))
        #     file.write()
        # file.write("}\n\n")

        for voice in chords:
            line = ""
            for i, note_num in enumerate(voice):
                note = to_note(note_num)
                line += str(note)
                if i == 0:
                    line += str(4)
                line += " "
            line += "|\n"
            print(line)
            file.write(line)
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
    progression, key, major_minor = get_progression()
    chords = get_voice_leading(progression, key, major_minor)
    # print(chords)
    # chords = [[2, 5, 9, 12], [5, 7, 11, 14], [4, 7, 11, 12]]
    generate_notation('notes.ly', chords, key, major_minor)
    open_pdf('notes.pdf')
