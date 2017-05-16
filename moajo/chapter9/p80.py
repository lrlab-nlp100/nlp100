#! /usr/bin/env python

# w.writeは適切にフラッシュされるぽい
# for line in fでループできてメモリも節約
def main():
    with open("enwiki-20150112-400-r10-105752.txt", "r", encoding="utf-8")as f:
        with open("p80_formatted.txt", "w", encoding="utf-8") as w:
            for line in f:
                words = line[:-1].split(" ")
                mapped = map(lambda w: w.strip(".,!?;:()[]'\""), words)
                ws = filter(lambda m: m != "", mapped)
                w.write(" ".join(ws) + "\n")
            return


if __name__ == "__main__":
    main()
