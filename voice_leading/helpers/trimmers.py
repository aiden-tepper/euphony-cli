# remove voicings where voices cross each other
def voice_cross(options):
    return [i for i in options if i[0] < i[1] < i[2] < i[3]]

# remove voicings where S, A, or T are more than an octave apart
def octave_apart(options):
    return [i for i in options if i[1] - i[0] <= 12 and i[2] - i[1] <= 12]

# remove voicings where S, A, or T move by more than a 3rd
def third_jump(prev, options):
    return [i for i in options if abs(prev[1] - i[1]) <= 4 and abs(prev[2] - i[2]) <= 4 and abs(prev[3] - i[3]) <= 4]

# remove voicings where any two voicings a 5th apart move in parallel (or contrary to another 5th)
def parallel_contrary_fifths(prev, options):
    trimmed = []
    fifths = []
    for a in range(4):
        for b in range(a+1, 4):
            interval = prev[b] - prev[a]
            if interval % 7 == 0:
                fifths.append((a, b))
    for curr in options:
        valid = True
        for (a, b) in fifths:
            interval = curr[b] - curr[a]
            if interval % 7 == 0:
                valid = False
        if valid:
            trimmed.append(curr)
    return trimmed

# remove voicings where any two voicings an octave apart move in parallel (or contrary to another octave)
def parallel_contrary_octaves(prev, options):
    trimmed = []
    fifths = []
    for a in range(4):
        for b in range(a+1, 4):
            interval = prev[b] - prev[a]
            if interval % 12 == 0:
                fifths.append((a, b))
    for curr in options:
        valid = True
        for (a, b) in fifths:
            interval = curr[b] - curr[a]
            if interval % 12 == 0:
                valid = False
        if valid:
            trimmed.append(curr)
    return trimmed

# if a voicing exists with a common tone, remove non-common tone voicings
def common_tone(prev, options):
    trimmed = []
    common_tone = False
    for curr in options:
        if prev[1] == curr[1] or prev[2] == curr[2] or prev[3] == curr[3]:
            common_tone = True
    if common_tone:
        for curr in options:
            if prev[1] == curr[1] or prev[2] == curr[2] or prev[3] == curr[3]:
                trimmed.append(curr)
    else:
        trimmed = options
    return(trimmed)   

def trim(prev, options):
    options = voice_cross(options)
    options = octave_apart(options)
    if prev:
        options = third_jump(prev, options)
        options = parallel_contrary_fifths(prev, options)
        options = parallel_contrary_octaves(prev, options)
        options = common_tone(prev, options)
    return options

if __name__ == "__main__":
    trim([14, 26, 29, 33], [[19, 23, 26, 31], [19, 26, 31, 35]])