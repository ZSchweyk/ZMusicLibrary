# MusicLibrary
A simple and intuitive music library to create notes, chords and all the different inversions associated with them, scales, intervals, and so much more.

Created by Zeyn Schweyk. Contact zschweyk@gmail.com for any questions.

Install:
```
pip install ZMusicLibrary
```

###
Note
=

Create a note object:
```
n = Note("C4")
```
Add an interval: returns a Note object
####
All the fundamental intervals. Includes intervals in greater octaves as well. 
* "P1", "A1", "m2", "M2", "A2", "m3", "M3", "P4", "A4", "D5", "P5", "A5", "m6", "M6", "A6", "D7", "m7", "M7"
```
n1 = Note("F#3") + "M2" # add a major 2nd (G#3)
n2 = Note("A6") - "P4" # subtract a perfect 4th (E5)
n3 = Note("Eb5") + "-M3" # add a negative major 3rd (Cb5)
n4 = Note("Eb5") - "-M6" # subtract a negative major 3rd (C6)
# Can perform arithmetic on intervals greater than a perfect 8th
# like a "M9" (major 9th), as long as it fits within the piano keyboard
```
Compare 2 notes: returns a str
```
n1 = Note("C4")
n2 = Note("Eb5")
print(n1.compare_with(n2)) # will print a "m10", minor 10th
```
Perform logical tests:
```
n1 = Note("F5")
n2 = Note("G5")
print(n1 == n2) # False
print(n1 < n2) # True
print(n1 <= n2) # True
print(n1 > n2) # False
print(n1 >= n2) # False
print(n1 != n2) # True
```
Simplify a note's notation: returns a new Note object
```
n = Note("C##4")
print(n.simplify_notation()) # prints Note(D4)
```
###
Chord
=
Create a pre-defined chord object:
####
Here are the following chord types, and the intervals that they consist of:
####
* "Maj": ["P1", "M3", "P5"]
* "Maj7": ["P1", "M3", "P5", "M7"]
* "Dom": ["P1", "M3", "P5", "m7"] 
* "Min": ["P1", "m3", "P5"]
* "Min7": ["P1", "m3", "P5", "m7"]
* "MinNat7": ["P1", "m3", "P5", "M7"]
* "Dim": ["P1", "m3", "D5"]
* "Dim7": ["P1", "m3", "D5", "D7"]
* "HDim7": ["P1", "m3", "D5", "m7"]
```
c = Chord(chord_type="Min", bass_note="E4") # bass_note can be a str or Note object
print(c) # prints Chord([Note(F4), Note(Ab4), Note(C5)])
```
Create a custom chord object:
```
c1 = Chord(list_of_notes=["F#4", "G#4", "A5", "C#4"])
print(c1) # prints Chord([Note(F#4), Note(G#4), Note(A5), Note(C#4), Note(F#5)])

# OR

c2 = Chord(list_of_notes=[Note("F#4"), Note("G#4"), Note("A5"), Note("C#4")])
print(c2) # prints Chord([Note(F#4), Note(G#4), Note(A5), Note(C#4), Note(F#5)])

print("Equal:", c1 == c2) # prints True
```

Loop through the notes of a chord:
```
c1 = Chord(chord_type="Dim7", bass_note="E4")
for note in c1:
    print(note)
```

Make a chord have n notes (works with predefined and custom chords): returns a new chord
```
c1 = Chord(chord_type="Maj", bass_note="B3")
c1 = c1.to_n_number_notes(5)
print(c1) # prints Chord([Note(B3), Note(D#3), Note(F#3), Note(B4), Note(D#4)])
```

Change the inversion of a chord (works with predefined and custom chords): returns a new chord
####
There is no limit on the number of inversions, although the chord will shift an octave higher at len(chord) inversions.
```
c1 = Chord(chord_type="Maj", bass_note="B3")
c1 = c1.inversion(2)
print(c1) # prints Chord([Note(F#3), Note(B4), Note(D#4)])
```

Combine to_n_number_notes and inversion:
```
c1 = Chord(chord_type="Maj", bass_note="B3")
c1 = c1.to_n_number_notes(4)
print(c1.inversion(1)) # prints Chord([Note(D#3), Note(F#3), Note(B4), Note(D#4)])

c2 = Chord(chord_type="Maj", bass_note="B3")
c2 = c2.inversion(1)
print(c2.to_n_number_notes(4)) # prints Chord([Note(D#3), Note(F#3), Note(B4), Note(D#4)])
```
Perform logical tests:
####
Compares the last note of each chord, except for == and !=, which compare the every note in each chord.
```
c1 = Chord(chord_type="Maj", bass_note="B3")
c1 = c1.to_n_number_notes(4)
c1 = c1.inversion(1)

c2 = Chord(chord_type="Maj", bass_note="B3")
c2 = c2.to_n_number_notes(4)
c2 = c2.inversion(2)

print(c1 < c2) # True
print(c1 <= c2) # True
print(c1 > c2) # False
print(c1 >= c2) # False
print(c1 == c2) # False
print(c1 != c2) # True
```

###
Scale
=
Create a pre-defined scale object:
####
Here are the following scale types, and the intervals that they consist of:
####
* "Maj": ["P1", "M2", "M3", "P4", "P5", "M6", "M7"]
* "Min": ["P1", "M2", "m3", "P4", "P5", "m6", "m7"]
* "Chromatic": ["P1", "A1", "M2", "A2", "M3", "P4", "A4", "P5", "A5", "M6", "A6", "M7"],
#####
* "HMin": ["P1", "M2", "m3", "P4", "P5", "m6", "M7"]
* "MMin": ["P1", "M2", "m3", "P4", "P5", "M6", "M7"]
#####
* "MinBlues": ["P1", "m3", "P4", "D5", "P5", "m7"]
* "MajBlues": ["P1", "M2", "m3", "M3", "P5", "M6"]
#####
* "MajPent": ['P1', 'M2', 'M3',       'P5', 'M6']
* "MinPent": ['P1',       'm3', 'P4', 'P5',       'm7']
#####
* 'Ionian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'M7']
* 'Dorian': ['P1', 'M2', 'm3', 'P4', 'P5', 'M6', 'm7']
* 'Phrygian': ['P1', 'm2', 'm3', 'P4', 'P5', 'm6', 'm7']
* 'Lydian': ['P1', 'M2', 'M3', 'A4', 'P5', 'M6', 'M7']
* 'Mixolydian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'm7']
* 'Aeolian': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'm7']
* 'Locrian': ['P1', 'm2', 'm3', 'P4', 'd5', 'm6', 'm7']

```
s1 = Scale(scale_type="HMin", start_note="D4")
print(s1) # prints Scale([Note(D4), Note(E4), Note(F4), Note(G4), Note(A5), Note(Bb5), Note(C#5)])
```
Create a custom Scale object:
```
s2 = Scale(list_of_notes=["D4", "Eb4", "F4", "G4", "A5", "Bb5", "C#5"])
print(s2) # prints Scale([Note(D4), Note(Eb4), Note(F4), Note(G4), Note(A5), Note(Bb5), Note(C#5)])
```
Loop through the notes of a scale:
```
s1 = Scale(scale_type="MinBlues", start_note="C4")
for note in s1:
    print(note)
```

Perform logical tests:
####
Compares the last note of each scale, except for == and !=, which compare the every note in each scale.
```
s1 = Scale(scale_type="MinBlues", start_note="C4")
s2 = Scale(scale_type="Lydian", start_note="D4")

print(s1 < s2) # True
print(s1 <= s2) # True
print(s1 > s2) # False
print(s1 >= s2) # False
print(s1 == s2) # False
print(s1 != s2) # True
```
