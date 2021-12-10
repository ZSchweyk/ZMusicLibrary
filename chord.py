from note import Note


class Chord(Note):
    def __init__(self, bass_note, chord_type, inversion):
        super().__init__(bass_note)


intervals = ["m2", "M2", "m3", "M3", "P4", "A4", "P5", "m6", "M6", "m7", "M7", "P8"]
