from note import Note
from chord_types import types_of_chords
from UsefulFunctions import *


class Chord:
    def __init__(self, bass_note, chord_type):
        self.bass_note = Note(bass_note) if isinstance(bass_note, str) else bass_note
        self.chord_type = chord_type
        try:
            self.chord_intervals = types_of_chords[chord_type]
        except KeyError:
            raise Exception("Chord \"{}\" does not exist. Here is a list of all the possible chords:\n{}"
                            .format(chord_type, types_of_chords.keys())) from None
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
            self.chord.append(self.chord[len(self.chord) - 3] + "P8")

    def __iter__(self):
        return iter(self.chord)

    def __contains__(self, item):
        if isinstance(item, str):
            return Note(item) in self.chord
        elif isinstance(item, Note):
            return item in self.chord
        else:
            raise Exception("{} is of incorrect type. Must be str or Note, not {}".format(item, type(item)))

    def __getitem__(self, i):
        return self.chord[i]

    def __delitem__(self, i):
        """Delete an item"""
        del self.chord[i]

    def __setitem__(self, i, val):
        # optional: self._acl_check(val)
        self.chord[i] = val

    def insert(self, i, val):
        # optional: self._acl_check(val)
        self.chord.insert(i, val)

    def append(self, val):
        self.insert(len(self.chord), val)

    def __len__(self):
        return len(self.chord)

    def __str__(self):
        return str(self.chord)

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.chord)

