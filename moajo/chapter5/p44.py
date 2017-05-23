#! /usr/bin/env python

from chapter5.p41 import read_chunks
from chapter5.class_chunk import Chunk
import os
from typing import List


def create_dot_file(sentence: List[Chunk]):
    content = ""
    for chunk in sentence:
        content += '"{0}";\n'.format(chunk.to_surface())
        if chunk.dst != -1:
            content += '"{0}" -- "{1}";\n'.format(chunk.to_surface(), sentence[chunk.dst].to_surface())
    return """graph "g" {{
    node [fontname="arialuni.ttf", fontsize=10]
      edge [
        dir = forward,               //エッジの矢印を指定する
      ];
      {0}
    }}""".format(content)


def generate_graph(sentence, out):
    dot = create_dot_file(sentence)
    with open('temp.dot', 'w', encoding="utf-8") as f:
        f.write(dot)

    os.system("dot -Kneato -Tjpg temp.dot -o " + out)


def main():
    sentence_array = read_chunks()
    for i in range(10,15):
        generate_graph(sentence_array[i], "p44_result_{0}.jpg".format(i))


if __name__ == "__main__":
    main()
