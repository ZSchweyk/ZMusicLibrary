from note import Note
from chord import Chord

c = Chord(chord_type="Dom", bass_note="C4")
print(c.inversion(1))
print(c.inversion(2))
print("root chord:", c)


