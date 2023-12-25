# remove voicings where voices cross each other
def voice_cross(options):
    return [i for i in options if i[0] < i[1] < i[2] < i[3]]

# remove voicings where S, A, or T are more than an octave apart
def octave_apart(options):
    return [i for i in options if i[1] - i[0] <= 12 and i[2] - i[1] <= 12]

# remove voicings where S, A, or T move by more than a 3rd
def third_jump(prev, options):
    return [i for i in options if abs(prev[1] - i[1]) <= 4 and abs(prev[2] - i[2]) <= 4 and abs(prev[3] - i[3]) <= 4]

# remove voicings where any two voicings a fifth apart move in parallel
def parallel_fifths(prev, options):
    trimmed = []
    fifths = []
    for a in range(4):
        for b in range(a+1, 4):
            if prev[b] - prev[a] == 7:
                fifths.append((a, b))
    for curr in options:
        valid = True
        for (a, b) in fifths:
            if curr[b] - curr[a] == 7:
                valid = False
        if valid:
            trimmed.append(curr)
    return trimmed

def trim(prev, options):
    options = voice_cross(options)
    options = octave_apart(options)
    if prev:
        options = third_jump(prev, options)
        options = parallel_fifths(prev, options)
    return options

if __name__ == "__main__":
    parallel_fifths([0, 2, 9, 100], [[0, 3, 10, 100], [0, 4, 10, 100]])