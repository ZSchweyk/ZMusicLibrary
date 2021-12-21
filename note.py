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
    intervals =         ["P1", "m2", "M2", "m3", "M3", "P4", "A4", "D5", "P5", "A5", "m6", "M6", "D7", "m7", "M7"]
    num_half_tones =    [   0,    1,    2,    3,    4,    5,    6,    6,    7,    8,    8,    9,    9,   10,   11]
    letter_increments = [   0,    1,    1,    2,    2,    3,    3,    4,    4,    4,    5,    5,    6,    6,    6]
    ##################

    final_intervals = []
    final_num_half_tones = []
    final_letter_increments = []
    continue_appending = True
    for i in range(0, 8):
        for interval, half_tone, increment in zip(intervals, num_half_tones, letter_increments):
            if continue_appending:
                result = interval[:-1] + str(int(interval[-1]) + i * 7)
                final_intervals.append(result)
                final_letter_increments.append(increment + i * 7)
                if result == "m52":
                    continue_appending = False
            result = half_tone + i * 12
            if result <= 87:
                final_num_half_tones.append(result)


    intervals = final_intervals
    num_half_tones = final_num_half_tones
    letter_increments = final_letter_increments

    intervals_values = {}
    for half_tone_num, interval in zip(num_half_tones, intervals):
        intervals_values[interval] = half_tone_num

    # ---------------------------------------------------------------------------------------------------------

    def __init__(self, note: str):
        note = note[0].upper() + note[1:]
        for note_num, official_note in self.keyboard_with_octaves.items():
            if note in official_note:
                self.note = note
                self.letter = note[0]
                if len(note) == 2:
                    self.accidental = ""
                elif len(note) == 3:
                    self.accidental = note[1]
                else:
                    self.accidental = note[1:3]
                self.number = note_num
                self.octave = note[-1]
                return
        raise Exception("Invalid Note: \"{}\"".format(note))

    def __str__(self):
        return "Note(" + str(self.note) + ")"

    def __repr__(self):
        # return "<{} {}>".format(self.__class__.__name__, self.note)
        return self.__str__()

    def __add__(self, intvl: str, operation="+"):
        try:
            if "-" in intvl:
                intvl = intvl[1:]
                interval_index = self.intervals.index(intvl)
                boolean = True
            else:
                interval_index = self.intervals.index(intvl)
                boolean = False
        except ValueError:
            raise Exception("Invalid interval \"{}\".".format(intvl)) from None
        # num_letters_to_add = get_val_with_index(self.letter_increments, interval_index)
        num_letters_to_add = self.letter_increments[interval_index] if not boolean else -1 * self.letter_increments[interval_index]
        num_half_steps_to_add = self.intervals_values[intvl] if not boolean else -1 * self.intervals_values[intvl]

        letter_index = self.letter_names.index(self.letter)

        proper_letter = \
            get_val_with_index(self.letter_names,
                               letter_index + num_letters_to_add if operation == "+" else letter_index - num_letters_to_add)

        try:
            elem_with_accidental_s = self.keyboard_with_octaves[
                self.number + num_half_steps_to_add if operation == "+" else self.number - num_half_steps_to_add]
        except KeyError:
            raise Exception("Note {} + {} is out of bounds.".format(self.note, intvl)) from None

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
        if self.number <= note.number:
            for interval in self.intervals:
                if self + interval == note:
                    return interval
        else:
            for interval in self.intervals:
                if self - interval == note:
                    return "-" + interval


