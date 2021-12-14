from UsefulFunctions import *


class Note:
    # -------------------------- Piano Keyboard ------------------------------------------------------------
    unique_notes = [
        ["G##", "A", "Bbb"],
        "",
        ["A##", "B", "Cb"],
        ["B#", "C", "Dbb"],
        "",
        ["C##", "D", "Ebb"],
        "",
        ["D##", "E", "Fb"],
        ["E#", "F", "Gbb"],
        "",
        ["F##", "G", "Abb"],
        ""
    ]
    flats = ["Bb", "Db", "Eb", "Gb", "Ab"]
    sharps = ["A#", "C#", "D#", "F#", "G#"]
    fill_in_list(unique_notes, [sharps, flats], "")

    keyboard_without_octaves = {}
    keyboard_with_octaves = {}
    octave = 1
    for i in range(88):
        note_index = i % len(unique_notes)
        note_s = unique_notes[note_index]
        num_appearances = count_appearances(list(keyboard_without_octaves.values()), note_s) + 1

        keyboard_without_octaves[i + 1] = note_s

        note_s_w_oct = []
        for note in note_s:
            note_s_w_oct.append(note + str(num_appearances))

        keyboard_with_octaves[i + 1] = note_s_w_oct

    del keyboard_without_octaves
    # ---------------------------------------------------------------------------------------------------------

    # --------------------------------- Intervals -------------------------------------------------------------
    letter_names = ["C", "D", "E", "F", "G", "A", "B"]
    intervals = ["P1", "m2", "M2", "m3", "M3", "P4", "A4", "D5", "P5", "A5", "m6", "M6", "D7", "m7", "M7", "P8"]
    num_half_tones = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 10, 11, 12]
    letter_increments = [0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7]
    ##################

    intervals_values = {}
    for half_tone_num, interval in zip(num_half_tones, intervals):
        intervals_values[interval] = half_tone_num

    # ---------------------------------------------------------------------------------------------------------

    def __init__(self, note: str):
        note = note[0].upper() + note[1:]
        for note_num, official_note in self.keyboard_with_octaves.items():
            if note in official_note:
                self.note = note
                self.number = note_num
                self.octave = note[-1]
                return
        raise Exception("Invalid Note: \"{}\"".format(note))

    def __str__(self):
        return str(self.note)

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.note)

    def __add__(self, intvl: str, operation="+"):
        try:
            interval_index = self.intervals.index(intvl)
        except ValueError:
            raise Exception("Invalid interval \"{}\".".format(intvl)) from None
        num_letters_to_add = self.letter_increments[interval_index]
        num_half_steps_to_add = self.intervals_values[intvl]

        letter_index = self.letter_names.index(self.note[0])

        proper_letter = \
            get_val_with_index(self.letter_names,
                               letter_index + num_letters_to_add if operation == "+" else letter_index - num_letters_to_add)

        try:
            elem_with_accidental_s = self.keyboard_with_octaves[
                self.number + num_half_steps_to_add if operation == "+" else self.number - num_half_steps_to_add]
        except KeyError:
            raise Exception("Note out of bounds.") from None

        for n in elem_with_accidental_s:
            if proper_letter in n:
                return Note(n)

    def __radd__(self, intvl: str):
        return self.__add__(intvl)

    def __sub__(self, intvl):
        return self.__add__(intvl, operation="-")

    def __rsub__(self, intvl):
        raise Exception("Invalid arithmetic order. \"{}\" must come after Note object.".format(intvl))

    def simplify_notation(self):
        """Returns a new Note object with simplified notation"""
        note_array = self.keyboard_with_octaves[self.number]
        return Note(note_array[1] if len(note_array) == 3 else self.note)

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number

    def __gt__(self, other):
        return self.number > other.number

    def __lt__(self, other):
        return self.number < other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __le__(self, other):
        return self.number <= other.number

    def compare_with(self, note):
        difference = self.number - note.number
        # Not done yet

