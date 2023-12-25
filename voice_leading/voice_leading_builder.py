from voice_leading.helpers.get_chord_notes import get_chord_notes
from voice_leading.helpers.trimmers import trim
from voice_leading.helpers.valid_permutations import get_valid_permutations
from play_prog import play

def voice_lead(chord_a, chord_b):
    # get all possible valid permutations of the current chord
    options = get_valid_permutations(chord_b)

    # remove illegal options
    options = trim(chord_a, options)

    # if only one option, skip
    if len(options) == 1:
        return options[0]

    # NOTE: FOR TESTING PURPOSES
    if chord_a:
        print('chord_a: ' + str(chord_a))
        print('chord_b: ' + str(chord_b))

    for i, voicing in enumerate(options, start=1):
        print(f"{i}) {voicing}")

    choice = int(input("Choose a voicing: "))
    print()
    return options[choice - 1]

def get_voice_leading(progression_as_str: list, key: str, major_minor: str) -> list:
    print(f'\nFull progression: {progression_as_str}')

    progression_as_matrix = [get_chord_notes(key, major_minor, chord) for chord in progression_as_str]
    print(f'\nProgression matrix: {progression_as_matrix}')

    voice_leading = []

    a = voice_lead(None, progression_as_matrix[0])
    voice_leading.append(a)

    for b in progression_as_matrix[1:]:
        a = voice_lead(a, b)
        voice_leading.append(a)

    return voice_leading

if __name__ == "__main__":
    # prog = get_voice_leading(['ii', 'V7', 'I7'], "C", "major")
    prog = get_voice_leading(['i', 'iv', 'V/V', 'V6/4', 'I', 'i', 'III', 'viidim/vi', 'VI7', 'iv7', 'V7', 'i'], "Ab", 'minor')
    print('prog: ' + str(prog))
    play(prog)
