# MusicLibrary
A simple and intuitive music library to create notes, chords and all the different inversions associated with them, scales, intervals, and so much more.
###
##Note

Create a note object:
```
n = Note("C4")
```
Add an interval: returns a Note object
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
##Chord
#####Documentation comming Soon...
#