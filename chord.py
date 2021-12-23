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
                                "of all possible chords:\n{}. Otherwise, create a custom chord with the list_of_notes"
                                "parameter."
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
        self._pop_note = True

    def to_n_number_notes(self, number):
        assert number > 0, "{} must be > 0.".format(number)
        if number <= len(self):
            return Chord(list_of_notes=self.chord[:number])
        else:
            self._pop_note = False
            new_chord = self.inversion(number - len(self))
            self._pop_note = True
            return new_chord

    def inversion(self, inversion_num):
        # assert inversion_num <= self.max_inversions, "Inversion {} exceeds the maximum " \
        # "inversion ({}) for {} {}!". \
        # format(inversion_num, self.max_inversions, self.bass_note.note, self.chord_type)

        chord_copy = self.chord.copy()

        for i in range(inversion_num):

            chord_letters = []
            for note in chord_copy:
                chord_letters.append(note.letter)

            index_to_append = (chord_letters.index(chord_letters[-1]) + 1) % len(chord_letters)
            chord_copy.append(chord_copy[index_to_append] + "P8")
            if self._pop_note: chord_copy.pop(0)

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

    def __eq__(self, other):
        if isinstance(other, Chord):
            return self.chord == other.chord
        else:
            raise Exception("{} is of incorrect type. Must be a Chord object.".format(other))

    def __ne__(self, other):
        if isinstance(other, Chord):
            return self.chord != other.chord
        else:
            raise Exception("{} is of incorrect type. Must be a Chord object.".format(other))

    def __gt__(self, other):
        if isinstance(other, Chord):
            return self[-1].number > other[-1].number
        else:
            raise Exception("{} is of incorrect type. Must be a Chord object.".format(other))

    def __lt__(self, other):
        if isinstance(other, Chord):
            return self[-1].number < other[-1].number
        else:
            raise Exception("{} is of incorrect type. Must be a Chord object.".format(other))

    def __ge__(self, other):
        if isinstance(other, Chord):
            return self[-1].number >= other[-1].number
        else:
            raise Exception("{} is of incorrect type. Must be a Chord object.".format(other))

    def __le__(self, other):
        if isinstance(other, Chord):
            return self[-1].number <= other[-1].number
        else:
            raise Exception("{} is of incorrect type. Must be a Chord object.".format(other))

    def __getitem__(self, i):
        self.chord_type = "custom"
        return self.chord[i]

    def __delitem__(self, i):
        self.chord_type = "custom"
        del self.chord[i]

    def __setitem__(self, i, val):
        if isinstance(val, Note):
            self.chord_type = "custom"
            self.chord[i] = val
        elif isinstance(val, str):
            self.chord_type = "custom"
            self.chord[i] = Note(val)
        else:
            raise Exception("{} is of incorrect type. Must be a Note or str object.".format(val))

    def insert(self, i, val):
        if isinstance(val, Note):
            self.chord_type = "custom"
            self.chord.insert(i, val)
        elif isinstance(val, str):
            self.chord_type = "custom"
            self.chord.insert(i, Note(val))
        else:
            raise Exception("{} is of incorrect type. Must be a Note or str object.".format(val))

    def append(self, val):
        if isinstance(val, Note):
            self.chord_type = "custom"
            self.insert(len(self.chord), val)
        elif isinstance(val, str):
            self.chord_type = "custom"
            self.insert(len(self.chord), Note(val))
        else:
            raise Exception("{} is of incorrect type. Must be a Note or str object.".format(val))

    def __len__(self):
        return len(self.chord)

    def __str__(self):
        return "Chord(" + str(self.chord) + ")"

    def __repr__(self):
        # return "<{} {}>".format(self.__class__.__name__, self.note)
        return self.__str__()
