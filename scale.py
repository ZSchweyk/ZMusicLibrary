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

    def __getitem__(self, i):
        return self.scale[i]

    def __delitem__(self, i):
        """Delete an item"""
        del self.scale[i]

    def __setitem__(self, i, val):
        # optional: self._acl_check(val)
        self.scale[i] = val

    def insert(self, i, val):
        # optional: self._acl_check(val)
        self.scale.insert(i, val)

    def append(self, val):
        self.insert(len(self.scale), val)

    def __len__(self):
        return len(self.scale)

    def __str__(self):
        return str(self.scale)

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.scale)

