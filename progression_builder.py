from chord_graphs import Major, Minor

def get_progression() -> str:
    # Start the interactive interface
    key = input("Enter the key (C#, Abm, ...):  ")
    curr = input("Enter the starting chord: ")
    progression = [curr]

    if "m" in key:
        Chart = Minor
    else:
        Chart = Major

    while True:
        print("\nCURRENT CHORD: ", curr)
        print("Possible next chords: ", list(Chart.neighbors(curr)))
        next = input("Enter the next chord (or \"done\"): ")
        if next == "done":
            break
        if next not in Chart.neighbors(curr):
            print("Invalid chord transition. Please try again.")
            continue
        progression.append(next)
        curr = next

    print("\nFull progression: ", progression)
    return progression, key
