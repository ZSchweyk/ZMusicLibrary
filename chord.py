from note import Note
from chord_types import types
from UsefulFunctions import *


class Chord:
    def __init__(self, bass_note, chord_type):
        self.bass_note = Note(bass_note)
        self.chord_type = chord_type
        self.chord_intervals = types[chord_type]

        self.chord = [self.bass_note + interval for interval in self.chord_intervals]
        self.max_inversions = len(self.chord) - 1
        self._index = -1

    def to_n_number_notes(self, number):
        new_notes = []
        for n in range(number):
            elem = get_val_with_index(self.chord, n)
            while elem in new_notes:
                elem += "P8"
            new_notes.append(elem)
        self.chord = new_notes


    def inversion(self, inversion_num):
        assert inversion_num <= len(self.chord) - 1, "Inversion {} exceeds the maximum inversion ({}) for {} {}!". \
            format(inversion_num, len(self.chord) - 1, self.bass_note, self.chord_type)

        # 3: 0
        # 4: 1
        # 5: 2

        for inversion in range(inversion_num):
            element_0 = self.chord.pop(0)
            self.chord.append(self.chord[inversion_num-3] + "P8")

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self.chord):
            self._index = -1
            raise StopIteration
        else:
            return self.chord[self._index]

    def __contains__(self, item):
        if isinstance(item, str):
            return Note(item) in self.chord
        elif isinstance(item, Note):
            return item in self.chord
        else:
            raise Exception("{} is of incorrect type. Must be str or Note, not {}".format(item, type(item)))

    def __repr__(self):
        t = str(type(self))
        start = t.index(".") + 1
        return t[start:-2] + "(" + str(self.chord) + ")"


c = Chord("C4", "Min")
print(c)
c.to_n_number_notes(4)
print(c)
c.inversion(1)
print(c)

intervals = ["m2", "M2", "m3", "M3", "P4", "A4", "P5", "m6", "M6", "m7", "M7", "P8"]
