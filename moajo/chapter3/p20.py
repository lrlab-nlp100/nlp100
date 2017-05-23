#! /usr/bin/env python


def read_eng() -> str:
    with open("jawiki-country.json", encoding="utf-8") as f:
        src = f.read()
        for line in src.split("\n"):
            if '"title": "イギリス"' in line:
                return line


def main():
    print(read_eng())


if __name__ == "__main__":
    main()
