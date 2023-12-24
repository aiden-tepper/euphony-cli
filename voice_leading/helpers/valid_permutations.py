from itertools import product, permutations

# establish absolute limits for each voice (S, A, T, B)
# 0 is defined as the low C four half-steps below the bottom of the bass range
lower_limits = [4, 12, 19, 24]
upper_limits = [24, 31, 38, 43]

def get_valid_permutations(chord):
    # create a list of the possible permutations of the chord
    # for now, each chord is assumed to be in root position
    all_poss = [p for p in permutations(chord) if p[0] == chord[0]]

    # next, for each permutation, we consider every version that fits within the voice ranges
    # we add each possibility to a list
    all_poss_within_range = []
    for poss in all_poss:
        curr_poss_within_range = []
        for num, lower_limit, upper_limit in zip(poss, lower_limits, upper_limits):
            i = 0
            result = []
            while num + 12 * i <= upper_limit:
                value = num + 12 * i
                if value >= lower_limit:
                    result.append(value)
                i += 1
            curr_poss_within_range.append(result)
        all_poss_within_range.append(curr_poss_within_range)

    combinations = []
    for c in all_poss_within_range:
        combinations.append(list(product(c[0], c[1], c[2], c[3])))
    combinations = [i for r in combinations for i in r]

    return [list(combination) for combination in combinations]