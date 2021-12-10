from note import Note
from chord_types import types


class Chord:
    def __init__(self, bass_note, chord_type, inversion="root"):
        self.bass_note = Note(bass_note)
        self.chord_type = chord_type
        self.chord_intervals = types[chord_type]
        self.max_inversions = len(self.chord_intervals) - 1
        self.inversion = inversion
        if self.inversion == "root":
            self.chord = [self.bass_note + interval for interval in self.chord_intervals]
        else:
            # Do inversions of intervals, or create root chord and then do inversions.
            pass


intervals = ["m2", "M2", "m3", "M3", "P4", "A4", "P5", "m6", "M6", "m7", "M7", "P8"]
