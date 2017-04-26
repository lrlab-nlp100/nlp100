class Morph:
    def __init__(self, surface: str, base: str, pos: str, pos1: str):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "{{suf:{0} bs:{1} pos:{2} pos1:{3}}}".format(self.surface, self.base, self.pos, self.pos1)

    def __repr__(self):
        return self.__str__()
