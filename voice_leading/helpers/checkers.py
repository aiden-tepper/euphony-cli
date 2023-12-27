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