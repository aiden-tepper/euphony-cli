from resources.chord_graphs import Major, Minor

def get_progression() -> str:
    # Start the interactive interface
    key = input("Enter the key (C#, Abm, ...):  ")
    curr = input("Enter the starting chord: ")
    progression = [curr]

    if "m" in key:
        Chart = Minor
        major_minor = "minor"
        key = key[:-1]
    else:
        Chart = Major
        major_minor = "major"

    while True:
        print("\nCURRENT CHORD: ", curr)
        if curr[-1] == "7":
            curr = curr[:-1]
        print("Possible next chords: ", list(Chart.neighbors(curr)))
        next = input("Enter the next chord (or \"done\"): ")
        valid = True
        # valid = False
        # if next in Chart.neighbors(curr):
        #     valid = True
        if next[-1] == "7" and next[:-1] in Chart.neighbors(curr):
            valid = True
        if next == "done":
            break
        if not valid:
            print("Invalid chord transition. Please try again.")
            continue
        progression.append(next)
        curr = next
    
    print("\nPROGRESSION: ", progression)

    return progression, key, major_minor
