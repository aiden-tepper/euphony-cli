# voice-leading-cmdline

*Command-line interface to explore voice leading paradigms for harmony in music composition for homorhythmic, homophonic texture*

for the given bassline, analyze the Roman numerals below the staff and add soprano, alto, and tenor parts in "chorale-style," following rules of good voice leading.
-- do the same in the "keyboard-style," where all three upper voices are in the treble clef.

for the given Roman numeral chord progression, create figured bass symbols and add all four voices in "chorale-style"

specify the six-four chord type
provide figured bass symbols
note harmonic function of chords in progression

## Workflow
enter either bassline, Roman numerals, or alphabetical chord progression
output full voicings as midi
option to print all 4 voices to one midi track or send each voice to separate track

## Rules
> The main concerns of composers writing homorhythmic, homophonic music were both unity and independence. This seems contrary at first. However, unity is a vertical dimension concern (the chords), while independence is a horizontal concern (the lines). Each of these concerns is addressed in princples of voice spacing.
> [Sun Music School](https://sunmusicschool.weebly.com/uploads/2/5/4/5/25453716/voice_leading.pdf)
* Unity
  * root position triads -- double the root
  * first inversion triads -- double the root or 5th, 3rd if absolutely necessary
  * second inversion triads -- double the 5th
  * seventh chords -- one voice for each note, omitting 5th if necessary
  * avoid doubling leading tone
  * never have more than an octave between adjacent voices in SAT
  * never have more than a 12th between T/B
  * avoid voice crossing
* Independence
  * keep common tones
  * move voices by step when possible, otherwise smallest possible interval (no more than a 3rd)
  * use contrary motion if possible (adjacent voices move in opposite directions)
  * avoid parallel fifths
  * avoid parallel fifths by contrary motion
  * avoid parallel octaves
  * avoid parallel octaves by contrary motion
  * avoid hidden/direct fifths and octaves
  * avoid using the +2 interval melodically
 
## Points of User Input
* SATB vs Keyboard Voicing
  * SATB keeps SA on treble staff and TB on bass staff, both open and close structure is okay
  * Keyboard voicing places SAT on treble staff and B on bass staff, close structure is most frequent
 
## Algorithm 
*(for root position chords)*
* Is chord a 4th or 5th away?
  * Common tone approach
    * move the bass to the root of the next chord
    * carry over the common tone from the previous chord
    * move the remaining voices by step or smallest possible interval
    * try to incorporate contrary motion
  * Non-common tone approach
    * move the bass to the root of the next chord
    * move all of the remaining voices to the nearest chord tone of the next chord
    * try to incorporate contrary motion
* Is chord a 3rd or 6th away?
  * move the bass to the root of the next chord
  * carry over the two common tones from the previous chord
  * move the remaining voice by step to complete the chord
* Is chord a 2nd away?
  * move the bass to the root of the next chord
  * in contrary motion to the bass, move the remaining voices to the nearest chord tone of the next chord

## Notes
*If no octave changing mark is used on a pitch, its octave is calculated so that the interval with the previous note is less than a fifth. As SAT will not move by an interval larger than a 3rd, this is only a concern for keeping B within range.*
### Voice Ranges
* Soprano
  * C4 - G5
  * C' - G''
  * Translated to relative C: C - G'
  * 20 - 39
* Alto
  * G3 - D5
  * G - D''
  * Translated to relative C: G, - D'
  * 15 - 34
* Tenor
  * C3 - G4
  * C - G'
  * 8 - 27
* Bass
  * E2 - C4
  * E, - C'
  * 0 - 20

## References
[Sun Music School](https://sunmusicschool.weebly.com/uploads/2/5/4/5/25453716/voice_leading.pdf)
