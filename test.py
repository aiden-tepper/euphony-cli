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

# input: a chord with either 3 or 4 notes
# output: a list of voicing options

# assume for now that each chord has 4 notes
#     B will always be the root note
#     S, A, and T will be permutations of the remaining 3 notes
#     that means that there should be 6 arrangements of chords returned
#         (357, 375, 537, 573, 735, 753)

# first, the absolute limits are established for each voice (S, A, T, B)
#     0 is defined as the low C four half-steps below the bottom of the bass range

lower_limits = [4, 12, 19, 24]
upper_limits = [24, 31, 38, 43]

# next, we find the chord notes

def get_chord_notes(key: str, major_minor: str, roman_numeral: str) -> list:
    chord = chord_mapping[roman_numeral]
    offset = key_to_num[key]
    if major_minor == "minor":
        offset = (offset - 3) % 12
    return [note + offset for note in chord]

chord = get_chord_notes("C", "major", "ii")
print(chord)

# next, we create a list of the possible permutations of the chord

permutations = [p for p in permutations(chord) if p[0] == chord[0]]
print(permutations)

# next, for each permutation, we consider every version that fits within the voice ranges
# we add each possibility to a list

x = []
for num, lower_limit, upper_limit in zip(chord, lower_limits, upper_limits):
    i = 0
    result = []
    while num + 12 * i <= upper_limit:
        value = num + 12 * i
        if value >= lower_limit:
            result.append(value)
        i += 1
    x.append(result)

print(x)

combinations = list(product(x[0], x[1], x[2], x[3]))
interpolated_lists = [list(combination) for combination in combinations]
print(interpolated_lists)

# now, we can start to pare down erroneous voicings
# first and most simple, we remove voicings where voices cross each other

no_voice_crossing = [i for i in interpolated_lists if i[0] < i[1] < i[2] < i[3]]
print("")
print(no_voice_crossing)

# from this point on, we can start to remove possibilities based on the rules of voice leading