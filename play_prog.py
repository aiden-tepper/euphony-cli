import time
import fluidsynth

def play_organ(chords):
    print('prog: ' + str(chords) + '\n')

    fs = fluidsynth.Synth()
    fs.start()
    fs.setting('synth.gain', 0.8)

    sfid = fs.sfload("resources/Gothorgn.sf2")
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
        time.sleep(1.5)

        fs.noteoff(0, S)
        fs.noteoff(0, A)
        fs.noteoff(0, T)
        fs.noteoff(0, B)
        time.sleep(0.1)

    fs.delete()

def play_piano(chords):
    print('prog: ' + str(chords) + '\n')

    fs = fluidsynth.Synth()
    fs.start()
    fs.setting('synth.gain', 0.8)

    sfid = fs.sfload("resources/TimGM6mb.sf2")
    fs.program_select(0, sfid, 0, 0)

    for chord in chords:
        print(f"playing chord: {chord}")
        [B, T, A, S] = chord
        B += 32
        T += 32
        A += 32
        S += 32
        fs.noteon(0, B, 100)
        time.sleep(0.01)
        fs.noteon(0, T, 90)
        time.sleep(0.01)
        fs.noteon(0, A, 85)
        time.sleep(0.01)
        fs.noteon(0, S, 80)
        time.sleep(0.47)

        fs.noteoff(0, T)
        time.sleep(0.01)
        fs.noteoff(0, A)
        time.sleep(0.01)
        fs.noteoff(0, S)
        time.sleep(0.18)

        fs.noteon(0, S, 70)
        fs.noteon(0, A, 75)
        fs.noteon(0, T, 80)
        time.sleep(0.37)

        fs.noteoff(0, B)
        time.sleep(0.1)
        fs.noteon(0, B, 100)
        time.sleep(0.23)
        fs.noteoff(0, B)

    fs.delete()

if __name__ == "__main__":
    chords = [[14, 26, 33, 41], [19, 26, 35, 43], [24, 28, 36, 43]]
    play(chords)