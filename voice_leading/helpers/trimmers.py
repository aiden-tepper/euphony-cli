# are two notes a 5th apart?
def fifth(a, b):
    for i in range(7, b - a + 1, 12):
        if b - a % i == 0:
            return True
    return False

# are two notes an 8ve apart?
def octave(a, b):
    return b - a % 12 == 0

# are two voices a and b moving in similar motion?
def similar_motion(prev, curr, a, b):
    diff_a = curr[a] - prev[a]
    diff_b = curr[b] - prev[b]
    return diff_a > 0 == diff_b > 0

# remove voicings where voices cross each other
def voice_cross(options):
    return [i for i in options if i[0] < i[1] < i[2] < i[3]]

# remove voicings where S, A, or T are more than an 8ve apart
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
            if fifth(prev[a], prev[b]):
                fifths.append((a, b))
    for curr in options:
        valid = True
        for (a, b) in fifths:
            if fifth(prev[a], prev[b]):
                valid = False
        if valid:
            trimmed.append(curr)
    return trimmed

# remove voicings where any two voicings an 8ve apart move in parallel (or contrary to another 8ve)
def parallel_contrary_octaves(prev, options):
    trimmed = []
    octaves = []
    for a in range(4):
        for b in range(a+1, 4):
            if octave(prev[a], prev[b]):
                octaves.append((a, b))
    for curr in options:
        valid = True
        for (a, b) in octaves:
            if octave(prev[a], prev[b]):
                valid = False
        if valid:
            trimmed.append(curr)
    return trimmed

# remove voicings where S and B move in similar motion to 5th
def hidden_fifths(prev, options):
    trimmed = []
    for curr in options:
        if similar_motion(prev, curr, 0, 3) and fifth(prev[0], prev[3]):
            continue
        trimmed.append(curr)
    return trimmed

# remove voicings where S and B move in similar motion to 8ve
def hidden_octaves(prev, options):
    trimmed = []
    for curr in options:
        if similar_motion(prev, curr, 0, 3) and octave(prev[0], prev[3]):
            continue
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

# last resort, favor voicings with more contrary motion
def contrary_motion(prev, options):
    max_score = 0
    best = None
    for curr in options:
        score = 0
        for i in range(4):
            for j in range(i+1, 4):
                if not similar_motion(prev, curr, i, j):
                    score += 1
        if score > max_score:
            max_score = score
            best = curr
        if score == max_score:
            print("fuck")
    return [best]

def further(count=[0]): 

    count[0]+=1

def trim(prev, options):
    options = voice_cross(options)
    options = octave_apart(options)
    if prev:
        options = third_jump(prev, options)
        options = parallel_contrary_fifths(prev, options)
        options = parallel_contrary_octaves(prev, options)
        options = hidden_fifths(prev, options)
        options = hidden_octaves(prev, options)
        options = common_tone(prev, options)
        if len(options) > 1:
            options = contrary_motion(prev, options)
    return options

if __name__ == "__main__":
    trim([14, 26, 29, 33], [[19, 23, 26, 31], [19, 26, 31, 35]])