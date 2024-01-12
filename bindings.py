from resources.chord_graphs import Major, Minor
from voice_leading.helpers.get_chord_notes import get_chord_notes
from voice_leading.voice_leading_builder import voice_lead
from lilypond.lilypond_builder import generate_notation
from play_prog import *
import subprocess

def next_chords(curr: str, key: str, major_minor: str) -> list:
    """
    Returns the possible next chords in the progression.
    """

    if major_minor == "minor":
        Chart = Minor
        key = key[:-1]
    else:
        Chart = Major
    
    return Chart.neighbors(curr)

def generate_progression(progression_as_str: list, key: str, major_minor: str) -> list:
    """
    Generates and returns the voice leading for the given progression.
    """

    progression_as_matrix = [get_chord_notes(key, major_minor, chord) for chord in progression_as_str]

    result = []

    a = voice_lead(None, progression_as_matrix[0])
    result.append(a)

    for b in progression_as_matrix[1:]:
        a = voice_lead(a, b)
        result.append(a)

    generate_sheet_music(result, key, major_minor)

    return result

def generate_sheet_music(progression: list, key: str, major_minor: str):
    generate_notation('../resources/notes.ly', progression, key, major_minor)
    # subprocess.call(['lilypond', '--output=../resources/notes', '../resources/notes.ly'])
    subprocess.call(['lilypond', '-fpng', '-dresolution=600', '-dpreview', '-o', '../resources/output', '../resources/notes.ly'])

def play_audio(chords: list):
    play_organ(chords)
    # play_piano(chords)