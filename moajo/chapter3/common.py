import sys


def get_end_index(str_: str, begin, end, start_pos):
    current_pos = start_pos+len(begin)
    while True:
        b_pos = str_.find(begin, current_pos)
        e_pos = str_.find(end, current_pos)
        if b_pos == -1 or e_pos < b_pos:
            return e_pos
        if b_pos < e_pos:
            current_pos = get_end_index(str_, begin, end, b_pos) + len(end)


def get_brace(str_: str, start_pos: int, begin="{", end="}") -> str:
    end_index = get_end_index(str_, begin, end,start_pos)
    return str_[start_pos:end_index + len(end)]
