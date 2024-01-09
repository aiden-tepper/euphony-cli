from voice_leading.voice_leading_builder import get_voice_leading
from play_prog import *

if __name__ == "__main__":
    # prog = get_voice_leading(['i', 'iv', 'V/V', 'V6/4', 'I', 'i', 'III', 'viidim/vi', 'VI7', 'iv7', 'V7', 'i'], "Ab", 'minor')
    # play_organ(prog)
    # play_piano(prog)
    play_piano([[7, 19, 26, 34], [17, 21, 29, 36], [10, 22, 29, 38], [15, 22, 31, 39], [15, 21, 31, 39], [14, 21, 30, 38], [14, 21, 30, 36], [7, 19, 26, 34]])