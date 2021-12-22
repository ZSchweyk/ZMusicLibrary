from note import Note
from chord_types import types_of_chords
from UsefulFunctions import *


class Chord:
    def __init__(self, chord_type="custom", bass_note="", list_of_notes=None):
        if chord_type != "custom":
            if bass_note != "":
                self.bass_note = Note(bass_note) if isinstance(bass_note, str) else bass_note
            else:
                raise Exception("base_note must be a Note/str representing the bass note of the chord.")
            self.chord_type = chord_type
            try:
                self.chord_intervals = types_of_chords[chord_type]
            except KeyError:
                raise Exception("Chord \"{}\" does not exist. Please create a chord that is in the following list"
                                "of all possible chords:\n{}"
                                .format(chord_type, types_of_chords.keys())) from None
            self.chord = [self.bass_note + interval for interval in self.chord_intervals]
        else:
            if list_of_notes is None or not isinstance(list_of_notes, list):
                raise Exception("list_of_notes must be a list of Note/str objects representing a custom chord.")
            self.chord = []
            for note in list_of_notes:
                if isinstance(note, Note):
                    self.chord.append(note)
                elif isinstance(note, str):
                    self.chord.append(Note(note))
                else:
                    raise Exception("{} must be a list of note/str objects.".format(list_of_notes))

            self.bass_note = self.chord[0]
            self.chord_type = chord_type

        self.max_inversions = len(self.chord) - 1

    def to_n_number_notes(self, number):
        new_notes = []
        for n in range(number):
            elem = get_val_with_index(self.chord, n)
            while elem in new_notes:
                elem += "P8"
            new_notes.append(elem)
        return Chord(list_of_notes=new_notes)

    def inversion(self, inversion_num):
        assert inversion_num <= self.max_inversions, "Inversion {} exceeds the maximum inversion ({}) for {} {}!". \
            format(inversion_num, self.max_inversions, self.bass_note.note, self.chord_type)
        # 3: 0
        # 4: 1
        # 5: 2

        # if not unique:
        # chord_copy.append(chord_copy[len(chord_copy) - 3] + "P8")
        # chord_copy.pop(0)

        chord_copy = self.chord.copy()
        unique_letters = []
        is_unique = True
        for note in chord_copy:
            if note.letter not in unique_letters:
                unique_letters.append(note.letter)
            else:
                is_unique = False

        if is_unique:
            for inversion in range(inversion_num):
                # print("appending", self.modified_chord[len(self.modified_chord) - 3] + "P8")
                chord_copy.append(chord_copy[0] + "P8")
                chord_copy.pop(0)
        else:
            for inversion in range(inversion_num):
                chord_copy.append(chord_copy[len(chord_copy) - 3] + "P8")
                chord_copy.pop(0)
        return Chord(list_of_notes=chord_copy)

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
        return "Chord(" + str(self.chord) + ")"

    # def __repr__(self):
    #     return "<{} {}>".format(self.__class__.__name__, self.chord)

