from voice_leading.voice_leading_builder import get_voice_leading
from play_prog import *

if __name__ == "__main__":
    prog = get_voice_leading(['i', 'iv', 'V/V', 'V6/4', 'I', 'i', 'III', 'viidim/vi', 'VI7', 'iv7', 'V7', 'i'], "Ab", 'minor')
    # play_organ(prog)
    play_piano(prog)
    # play_organ([[12, 21, 24, 29], [5, 17, 24, 33]])