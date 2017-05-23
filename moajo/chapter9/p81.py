#! /usr/bin/env python

# w.writeは適切にフラッシュされるぽい
# for line in fでループできてメモリも節約
def main():
    with open("p81_countries.txt", "r", encoding="utf-8")as countries:
        hash_ = map(lambda line: (line[:-1], line[:-1].replace(" ", "_")), countries)  # last word is \n
        hash_ = filter(lambda c: c[0] != c[1], hash_)
        cs = []
        # print(hash_)
        for a in hash_:
            print(a)
            cs.append(a)
        with open("p80_formatted.txt", "r", encoding="utf-8")as formatted:
            with open("p81_replaced.txt", "w", encoding="utf-8") as w:
                for line in formatted:
                    for c in cs:
                        line = line.replace(c[0], c[1])
                    w.write(line)


if __name__ == "__main__":
    main()
