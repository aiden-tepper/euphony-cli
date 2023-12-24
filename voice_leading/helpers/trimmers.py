# remove voicings where voices cross each other
def voice_cross(options):
    return [i for i in options if i[0] < i[1] < i[2] < i[3]]

# remove voicings where S, A, or T are more than an octave apart
def octave_apart(options):
    return [i for i in options if i[1] - i[0] <= 12 and i[2] - i[1] <= 12]

# remove voicings where S, A, or T move by more than a 3rd
def third_jump(prev, options):
    return [i for i in options if abs(prev[1] - i[1]) <= 4 and abs(prev[2] - i[2]) <= 4 and abs(prev[3] - i[3]) <= 4]

def trim(prev, options):
    options = voice_cross(options)
    options = octave_apart(options)
    if prev:
        options = third_jump(prev, options)
    return options