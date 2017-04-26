from chapter5.class_morph import Morph
from typing import List


class Chunk:
    def __init__(self, morphs: List[Morph], dst: int, srcs: List[int]):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return "{{dst:{0} srcs:{1} morphs:{2}}}".format(self.dst, self.srcs, self.morphs)

    def __repr__(self):
        return self.__str__()
