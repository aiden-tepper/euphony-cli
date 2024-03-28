# Euphony-CLI

Euphony-CLI is a command-line tool designed for composers, musicians, music theory enthusiasts, songwriters, and music producers. This tool aids in exploring voice leading paradigms for harmony in homorhythmic, homophonic textures. Built in Python and inspired by manual voice leading construction algorithms, Euphony-CLI walks users through creating harmonically sound chord progressions using Roman numeral notation, then algorithmically generates four-part voice leading, draws it on a grand staff and exports to a PDF, and audibly plays the progression using a luscious organ soundfont.

I enjoy writing and producing music as a hobby, and the inspiration for this project came from a frustration with the time-intensive process of writing layered parts that abide by classic music theory rules (through a painstaking manual process I learned and partially forgot years ago). This tool does the dirty work for me, allowing for much higher levels of efficiency and much fewer breakages of my creative flow. On top of being useful for composing harmony, I have found this tool incredibly fun to use for brainstorming, as it is easy to generate new ideas and force myself to think outside of the box when it comes to creating progressions themselves -- the ability to quickly not only generate outrageous chord lines but listen to what it might sound like harmonized across multiple voices is a constant source of inspiration.

## Getting Started

### Prerequisites

- Python 3 installed on your system.
- LilyPond and FluidSynth manually installed for PDF export and audio playback, respectively.

### Installation

1. Clone the repository to your local machine.
2. Create a virtual environment with `python -m venv .venv` and activate it using `source .venv/bin/activate`.
3. Install the required Python libraries with `pip install -r requirements.txt`.

### Running Euphony-CLI

Start the program by running `python main.py` from the command line. The application will interactively guide you through setting the key of the progression and creating a chord progression.

## Features

Euphony-CLI currently offers a streamlined, user-friendly interface for generating chord progressions. Planned future updates include:

- **Custom Soundfonts**: Allow users to select custom soundfonts for playback.
- **PDF Output Settings**: Customize the appearance of the exported PDF, such as page margins and font size.
- **Time Signature and Note Lengths**: Adjust the time signature and note lengths for more control over the musical output.
- **Verbose Output**: Enable verbose output for detailed information during operation.
- **Advanced Mode**: For experienced users, provide more control over voice leading and access to advanced chord options.
- **Random Progression Generation**: For finding inspiration through generating and iterating through wild ideas

## Integration

Euphony-CLI integrates with LilyPond for generating musical scores in PDF format and FluidSynth for real-time audio playback of the generated chord progressions. This approach combines the visual and auditory exploration of music composition and theory for multi-modal output.

## Contributing

I welcome contributions from the community! Whether you're fixing a bug, adding a new feature, or improving the documentation, your help is appreciated. Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please make sure your code adheres to the project's coding standards (undergraduate level or higher I suppose) and passes all the tests (feel free but not compelled to write tests).

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Thanks to the developers and communities behind Python, LilyPond, and FluidSynth for creating and maintaining these powerful tools that make Euphony-CLI possible.
- A special shoutout to the music theory community and my previous music theory professors for providing the inspiration and knowledge that fuel this project.

## Audio Plugin Progress

A JUCE-based audio plugin is currently in development (by myself), in which the program's features can be used via a GUI and MIDI can be easily generated and dragged into projects. The JUCE library would allow shipping of the plugin binaries to all major DAWs through AAX, AU, and VST plugin formats. This next phase of the project quickly blew up in scope, and if you're interested in getting involed, please feel free to reach out!

You can track my current work at (https://github.com/aiden-tepper/euphony)[https://github.com/aiden-tepper/euphony].

## Future Plans

- **Integration with MusicXML**: For wider compatibility with music notation software.
- **Expanded Harmony Options**: Including more exotic chords and voice leading techniques.
- **User Interface Enhancements**: To make Euphony-CLI even more intuitive and powerful.
- **Collaboration Features**: Enabling multiple users to work on harmony lines simultaneously.

Stay tuned for updates as I continue to develop Euphony-CLI into an even more versatile tool for music composition, production, and education.

## Reference

### Rules

> The main concerns of composers writing homorhythmic, homophonic music were both unity and independence. This seems contrary at first. However, unity is a vertical dimension concern (the chords), while independence is a horizontal concern (the lines). Each of these concerns is addressed in princples of voice spacing.
> [Sun Music School](https://sunmusicschool.weebly.com/uploads/2/5/4/5/25453716/voice_leading.pdf)
* Unity
  * root position triads -- double the root (bass)
  * first inversion triads -- double the root or 5th, 3rd (bass) if absolutely necessary (try not to)
    * Exception: viidim6 and iidim6: double the 3rd (bass)
    * Exception: consecutive first inversion chords, alternate between doubling and not doubling the 3rd (bass)
  * second inversion triads -- double the 5th (bass)
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
  
### Algorithm 

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

### Notes

*If no octave changing mark is used on a pitch, its octave is calculated so that the interval with the previous note is less than a fifth. As SAT will not move by an interval larger than a 3rd, this is only a concern for keeping B within range.*

#### Voice Ranges

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

### Links

[Sun Music School](https://sunmusicschool.weebly.com/uploads/2/5/4/5/25453716/voice_leading.pdf)
[Puget Sound Music Theory](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html)
