import sys

argv = sys.argv

if len(argv) != 3:
    print("引数が足りません。few arguments")
    sys.exit()

with open(argv[1], encoding="utf-8") as f:
    lines = 0
    for line in f:
        lines += 1

    f.seek(0)
    count = 0
    n = int(argv[2])
    divline = lines // n
    file_index = 0
    line_count = 0
    dest = open("div"+str(file_index)+".txt", "w", encoding="utf-8")
    for line in f:
        line_count += 1
        count += 1
        dest.write(line)
        if count == divline:
            dest.close()
            file_index += 1
            if line_count != lines:
                dest = open("div"+str(file_index)+".txt", "w", encoding="utf-8")
            count = 0
    dest.close()

# split -l/N hightemp.txt (ファイルサイズに対してN分割(行を分割しない)
# echo "scale=0"; `cat hightemp.txt | wc -l '/3"
# バッククオート、bc
