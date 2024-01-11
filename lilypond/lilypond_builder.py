import textwrap
import subprocess

num_to_note_flats = {
    0: 'c', 1: 'des', 2: 'd',
    3: 'ees', 4: 'e', 5: 'f',
    6: 'ges', 7: 'g', 8: 'aes',
    9: 'a', 10: 'bes', 11: 'b'
}

num_to_note_sharps = {
    0: 'c', 1: 'cis', 2: 'd',
    3: 'dis', 4: 'e', 5: 'f',
    6: 'fis', 7: 'g', 8: 'gis',
    9: 'a', 10: 'ais', 11: 'b'
}

note_mapping = {
    'C': 'c', 'C#': 'cis', 'Db': 'des',
    'D': 'd', 'D#': 'dis', 'Eb': 'ees',
    'E': 'e', 'F': 'f', 'F#': 'fis',
    'Gb': 'ges', 'G': 'g', 'G#': 'gis',
    'Ab': 'aes', 'A': 'a', 'A#': 'ais',
    'Bb': 'bes', 'B': 'b'
}

def to_note(note_num, sharp) -> str:
    if sharp:
        num_to_note = num_to_note_sharps
    else:
        num_to_note = num_to_note_flats
    note = num_to_note[note_num % 12]
    for _ in range(int(note_num / 12)):
        note += "'"
    return note

def generate_notation(filename, chords, key, major_minor):
    with open(filename, 'w') as file:
        # Global settings

        global_string = textwrap.dedent(f'''\
            global = {{
              \\key {note_mapping[key]} \\{major_minor}
              \\time 4/4
              \\version "2.22.1"
            }}\n\n''')

        file.write(global_string)

        # transpose the chords list
        chords = list(zip(*chords))
        chords = reversed(chords)

        # determine if the key signature is sharp or flat
        if major_minor == 'major':
          if key in ['C' 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']:
            sharp = True
          else:
            sharp = False
        else:
          if key in ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#']:
            sharp = True
          else:
            sharp = False
            

        file.write("\\parallelMusic voiceA,voiceB,voiceC,voiceD {\n")
        for voice in chords:
            line = ""
            for i, note_num in enumerate(voice):
                note = to_note(note_num, sharp)
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
                 \\fixed c \\voiceA
                 \\\\
                 \\fixed c,  \\voiceB
               >>
             }
             \\new Staff {
               \\global \\clef bass
               <<
                 \\fixed c, \\voiceC
                 \\\\
                 \\fixed c, \\voiceD
               >>
             }
          >>
        }
        ''')
