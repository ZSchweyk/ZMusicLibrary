from scale import Scale
from chord import Chord
from note import Note

s1 = Scale(scale_type="MinBlues", start_note="C4")
s2 = Scale(scale_type="Lydian", start_note="D4")

print(s1 < s2) # True
print(s1 <= s2) # True
print(s1 > s2) # False
print(s1 >= s2) # False
print(s1 == s2) # False
print(s1 != s2) # True