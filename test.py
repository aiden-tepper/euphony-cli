from voice_leading.voice_leading_builder import get_voice_leading
from play_prog import play

if __name__ == "__main__":
    prog = get_voice_leading(['i', 'iv', 'V/V', 'V6/4', 'I', 'i', 'III', 'viidim/vi', 'VI7', 'iv7', 'V7', 'i'], "Ab", 'minor')
    # play_organ(prog)
    play_piano(prog)

    # play([[12, 21, 24, 29], [5, 17, 24, 33]])

# what's going on with lilypond

# what to do about picardy cadence?
# chord_a: [12, 21, 24, 29]
# chord_b: [5, 5, 9, 12]
# 1) [5, 17, 24, 33]
# 2) [17, 21, 24, 29]
    
# how to avoid hidden/direct 5ths/octaves?

# any way to trim based on leading tones (7th chords resolving)?