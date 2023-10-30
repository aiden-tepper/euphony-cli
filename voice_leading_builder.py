def octave_transform(input_chord, root):
    # Squish notes into a single octave and sort from lowest to highest
    return sorted([(root + (x % 12)) for x in input_chord])

def t_matrix(chord_a, chord_b):
    # Get the distances between the notes of two chords
    root = chord_a[0]
    chord_a_transformed = octave_transform(chord_a, root)
    chord_b_transformed = octave_transform(chord_b, root)
    return [b - a for a, b in zip(chord_a_transformed, chord_b_transformed)]

def voice_lead(chord_a, chord_b):
    # Voice lead from chord_a to chord_b
    root = chord_a[0]

    # Calculate the mapping of notes in chord_a to the sorted version
    a_leadings = [(x, octave_transform(chord_a, root).index(root + (x % 12))) for x in chord_a]
    
    # Calculate the t_matrix
    t_matrix_ab = t_matrix(chord_a, chord_b)
    
    # Calculate the new voicing for chord_b
    b_voicing = [x + t_matrix_ab[y] for (x, y) in a_leadings]
    
    return b_voicing

# Example chord progression
chord_progression = [
    [64, 67, 71],  # Chord E5 Minor
    [60, 64, 67],  # Chord C5 Major
    [66, 69, 71],  # Chord Fs5 Minor
    [71, 74, 79]   # Chord B5 Minor
]

from time import sleep

# Initialize the last chord to None
last_c = None

for a, b in zip(chord_progression, chord_progression[1:]):
    if last_c is None:
        # Play the first chord
        print("Playing:", a)
        last_c = a
        sleep(1)
    
    # Perform voice leading to transition from a to b
    last_c = voice_lead(last_c, b)
    
    print("Playing:", last_c)
    sleep(1)

# TODO
def get_voice_leading(progression: list, key: str) -> list:
    return []