import time
import fluidsynth

def play(chords):
    print('prog: ' + str(chords) + '\n')

    fs = fluidsynth.Synth()
    fs.start()
    fs.setting('synth.gain', 0.8)

    sfid = fs.sfload("resources/Gothorgn.sf2")
    # sfid = fs.sfload("resources/TimGM6mb.sf2")
    fs.program_select(0, sfid, 0, 0)

    for chord in chords:
        print(f"playing chord: {chord}")
        [B, T, A, S] = chord
        B += 24
        T += 24
        A += 24
        S += 24
        fs.noteon(0, S, 100)
        fs.noteon(0, A, 100)
        fs.noteon(0, T, 100)
        fs.noteon(0, B, 100)
        time.sleep(2.0)

        fs.noteoff(0, S)
        fs.noteoff(0, A)
        fs.noteoff(0, T)
        fs.noteoff(0, B)

    fs.delete()

if __name__ == "__main__":
    chords = [[14, 26, 33, 41], [19, 26, 35, 43], [24, 28, 36, 43]]
    play(chords)