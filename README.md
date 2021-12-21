# MusicLibrary
A simple, intuitive music library to create notes, chords, scales, intervals, and so much more.

Create a note:
```
n = Note("C4")
```
Add an interval:
```
n1 = Note("F#3") + "M2" # add a major 2nd
n2 = Note("A6") - "P4" # subtract a perfect 4th
n3 = Note("Eb5") + "-M3" # add a negative major 3rd
```
Compare 2 notes:
