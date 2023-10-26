import subprocess
import os
import sys
import textwrap

global_data = {
    "key": "c",
    "time_signature": "4/4"
}

##def get_lilypond_notation(notes):
##    # map user input to LilyPond syntax
##    note_mapping = {
##        "A": "a",
##        "B": "b",
##        "C": "c",
##        "D": "d",
##        "E": "e",
##        "F": "f",
##        "G": "g"
##    }

##    return " ".join(note_mapping[note.upper()] for note in notes.split())

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
##    lilypond_notation = get_lilypond_notation(notes)
    bassline = notes.split()

    with open('notes.ly', 'w') as file:
        # Global settings

        global_string = textwrap.dedent(f'''\
            global = {{
              \\key {global_data["key"]} \\major
              \\time {global_data["time_signature"]}
            }}\n\n''')

        file.write(global_string)

        # Voices
        
        file.write("\\parallelMusic voiceA,voiceB,voiceC,voiceD {{\n")
        for i, note in enumerate(bassline):
            if i % 4 == 0:
                file.write("  % Bar {}\n".format(i // 4 + 1))
            file.write("  {}8    ".format(note))
            if (i + 1) % 4 == 0 or i == len(bassline) - 1:
                file.write("|\n")
        file.write("}}\n\n")

        file.write("\\score {\n")
        file.write("  \\new PianoStaff <<\n")
        file.write("     \\new Staff {\n")
        file.write("       \\global\n")
        file.write("       <<\n")
        file.write("         \\relative c'' \\voiceA\n")
        file.write("         \\\\\n")
        file.write("         \\relative c'  \\voiceB\n")
        file.write("       >>\n")
        file.write("     }\n")
        file.write("     \\new Staff {\n")
        file.write("       \\global \\clef bass\n")
        file.write("       <<\n")
        file.write("         \\relative c \\voiceC\n")
        file.write("         \\\\\n")
        file.write("         \\relative c \\voiceD\n")
        file.write("       >>\n")
        file.write("     }\n")
        file.write("  >>\n")
        file.write("}\n")
        

    generate_notation('notes.ly')
    open_pdf('notes.pdf')
