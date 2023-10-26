import subprocess
import os
import sys
import textwrap

global_data = {
    "key": "c",
    "time_signature": "4/4"
}

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

   return [note_mapping[note.upper()] for note in notes]

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

        # Voices

#   a4    b     c   d     |
#   b4    c     d    e     |
#   c4   d     e    f     |
#   d4    e     f    g     |

#   e8      fis  g     a   |
#   fis4         g         |
#   e16 fis g  a fis g a b |
#   a4           a         |

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
    bassline = input("Enter musical notes separated by space: ")

    b = get_lilypond_notation(bassline.split())
    t = shift_notes(b, 4)
    a = shift_notes(b, 7)
    s = shift_notes(b, 11)
    notes = [s, a, t, b]
        
    generate_notation('notes.ly', notes)
    open_pdf('notes.pdf')
