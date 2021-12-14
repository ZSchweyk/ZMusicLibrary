from note import Note
from scale_types import types_of_scales


class Scale:
    def __init__(self, start_note, scale_type):
        self.start_note = Note(start_note) if isinstance(start_note, str) else start_note
        try:
            self.scale_type = scale_type
            self.scale_intervals = types_of_scales[scale_type]
        except KeyError:
            raise Exception("Scale \"{}\" does not exist. Here is a list of all the possible chords:\n{}"
                            .format(scale_type, types_of_scales.keys())) from None

        self.scale = [self.start_note + interval for interval in self.scale_intervals]
        self._index = 1

    def __contains__(self, item):
        if isinstance(item, Note):
            return item in self.scale
        elif isinstance(item, str):
            return Note(item) in self.scale
        else:
            raise Exception("{} is of incorrect type. Must be str or Note, not {}".format(item, type(item)))

    def __iter__(self):
        return iter(self.scale)

    def __repr__(self):
        return str(self.scale)


s = Scale("F#4", "HMin")
for note in s:
    print(note)
