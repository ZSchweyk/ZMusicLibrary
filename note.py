
def fill_in_list(array: list, values_to_replace_with_2d_array: list, value_to_replace):
    count = 0
    while value_to_replace in array:
        index = array.index(value_to_replace)
        array[index] = [arr[count] for arr in values_to_replace_with_2d_array]
        count += 1
    return array


def count_appearances(array, value):
    return 0 if len(array) == 0 else sum([item == value for item in array])


def get_val_with_index(array, index):
    index = index % len(array)
    return array[index]


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
        if isinstance(note_s, str):
            note_s_w_oct = note_s + str(num_appearances)
        else:
            note_s_w_oct = []
            for note in note_s:
                note_s_w_oct.append(note + str(num_appearances))

        keyboard_with_octaves[i + 1] = note_s_w_oct

    # ---------------------------------------------------------------------------------------------------------

    # --------------------------------- Intervals -------------------------------------------------------------
    letter_names = ["C", "D", "E", "F", "G", "A", "B"]
    intervals =           ["m2", "M2", "m3", "M3", "P4", "A4", "P5", "m6", "M6", "m7", "M7", "P8"]
    interval_increments = [   1,    1,    2,    2,    3,    3,    4,    5,    5,    6,    6,    7]
    intervals_values = {}
    for increment, interval in enumerate(intervals):
        intervals_values[interval] = increment + 1

    # ---------------------------------------------------------------------------------------------------------

    def __init__(self, note: str):
        note = note[0].upper() + note[1:]
        for note_num, official_note in self.keyboard_with_octaves.items():
            if note in official_note and (isinstance(official_note, list) or note == official_note):
                self.note = note
                self.number = note_num
                self.octave = note[-1]
                return
        # raise Exception("Invalid Note > \"{}\"".format(note))

    def __repr__(self):
        return self.note

    def __add__(self, intvl: str, operation="+"):
        interval_index = self.intervals.index(intvl)
        num_letters_to_add = self.interval_increments[interval_index]
        num_half_steps_to_add = self.intervals_values[intvl]

        letter_index = self.letter_names.index(self.note[0])

        proper_letter = \
            get_val_with_index(self.letter_names,
                    letter_index + num_letters_to_add if operation == "+" else letter_index - num_letters_to_add)
        print("proper_letter:", proper_letter)

        elem_with_accidental_s = self.keyboard_with_octaves[
            self.number + num_half_steps_to_add if operation == "+" else self.number - num_half_steps_to_add]

        print("elem_with_accidental_s:", elem_with_accidental_s)

        if isinstance(elem_with_accidental_s, list):
            for n in elem_with_accidental_s:
                if proper_letter in n:
                    return Note(n)
        else:
            return Note(elem_with_accidental_s)

    def __radd__(self, intvl: str):
        return self.__add__(intvl)

    def __sub__(self, intvl):
        return self.__add__(intvl, operation="-")

    def __rsub__(self, intvl):
        raise Exception("Invalid arithmetic order. \"{}\" must come after Note object.".format(intvl))


intervals = ["m2", "M2", "m3", "M3", "P4", "A4", "P5", "m6", "M6", "m7", "M7", "P8"]

print(Note("C#4") + "M3")



# get_val_with_index(["C", "D", "E", "F", "G", "A", "B"], )
