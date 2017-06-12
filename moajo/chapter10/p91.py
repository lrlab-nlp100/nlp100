#!/usr/bin/env python

# w.writeは適切にフラッシュされるぽい
# for line in fでループできてメモリも節約
def main():
    with open("questions-words.txt", "r", encoding="utf-8")as f:
        with open("p91_family.txt", "w", encoding="utf-8") as w:
            flag=False
            for line in f:
                if line.startswith(": family"):
                    flag=True
                    continue
                if flag:
                    if line.startswith(":"):
                        return
                    w.write(line)

if __name__ == "__main__":
    main()
