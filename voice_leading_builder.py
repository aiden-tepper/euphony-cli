from itertools import product, permutations

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
    "ii": [2, 5, 9, 12],
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

key_to_num = {
    'C': 0, 'C#': 1, 'Db': 1,
    'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'F': 5, 'F#': 6,
    'Gb': 6, 'G': 7, 'G#': 8,
    'Ab': 8, 'A': 9, 'A#': 10,
    'Bb': 10, 'B': 11
}

# establish absolute limits for each voice (S, A, T, B)
# 0 is defined as the low C four half-steps below the bottom of the bass range
lower_limits = [4, 12, 19, 24]
upper_limits = [24, 31, 38, 43]

def get_chord_notes(key: str, major_minor: str, roman_numeral: str) -> list:
    chord = chord_mapping[roman_numeral]
    offset = key_to_num[key]
    if major_minor == "minor":
        offset = (offset - 3) % 12
    return [note + offset for note in chord]

def voice_lead(chord_a, chord_b):
    # create a list of the possible permutations of the chord
    all_poss = [p for p in permutations(chord_b) if p[0] == chord_b[0]]

    # next, for each permutation, we consider every version that fits within the voice ranges
    # we add each possibility to a list
    all_poss_within_range = []
    for poss in all_poss:
        curr_poss_within_range = []
        for num, lower_limit, upper_limit in zip(poss, lower_limits, upper_limits):
            i = 0
            result = []
            while num + 12 * i <= upper_limit:
                value = num + 12 * i
                if value >= lower_limit:
                    result.append(value)
                i += 1
            curr_poss_within_range.append(result)
        all_poss_within_range.append(curr_poss_within_range)

    combinations = []
    for c in all_poss_within_range:
        combinations.append(list(product(c[0], c[1], c[2], c[3])))
    combinations = [i for r in combinations for i in r]
    interpolated_lists = [list(combination) for combination in combinations]

    # remove voicings where voices cross each other
    options = [i for i in interpolated_lists if i[0] < i[1] < i[2] < i[3]]

    # remove voicings where S, A, or T are more than an octave apart
    options = [i for i in options if i[1] - i[0] <= 12 and i[2] - i[1] <= 12]

    # remove voicings where S, A, or T move by more than a 3rd
    if chord_a:
        options = [i for i in options if abs(chord_a[1] - i[1]) <= 4 and abs(chord_a[2] - i[2]) <= 4 and abs(chord_a[3] - i[3]) <= 4]

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
    prog = get_voice_leading(['ii', 'V', 'I'], "C", "major")
    print('prog: ' + str(prog))
