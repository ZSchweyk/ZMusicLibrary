from scale import Scale
from chord import Chord
from note import Note

start = Note("C4")
array = []
intervals = ["P1", "A1", "M2", "A2", "M3", "P4", "A4", "P5", "A5", "M6", "A6", "M7"]
for interval in intervals:
    array.append(start + interval)

print(array)