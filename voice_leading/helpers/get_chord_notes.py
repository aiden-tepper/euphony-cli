from resources.chord_mappings import *

key_to_num = {
    'C': 0, 'C#': 1, 'Db': 1,
    'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'F': 5, 'F#': 6,
    'Gb': 6, 'G': 7, 'G#': 8,
    'Ab': 8, 'A': 9, 'A#': 10,
    'Bb': 10, 'B': 11
}

def get_chord_notes(key: str, major_minor: str, roman_numeral: str) -> list:
    if roman_numeral[-1] == "7":
        chord = chord_mapping_sevenths[roman_numeral[:-1]]
    else:
        chord = chord_mapping[roman_numeral]
        chord = [chord[0]] + chord
    offset = key_to_num[key]
    if major_minor == "minor":
        offset = (offset - 3) % 12
    return [note + offset for note in chord]