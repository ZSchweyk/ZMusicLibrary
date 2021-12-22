from note import Note
from chord import Chord

c = Chord(chord_type="Min", bass_note="C4")
c = c.to_n_number_notes(5)
print("root chord:", c)
print(c.inversion(1))
print(c.inversion(2))



