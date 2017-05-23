# -*- coding: utf-8 -*-
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

def split_file(write_file_name_head, file_name, n):
    with open(file_name, "r")as file:
        list = []
        for line in file:
            list.append(line)
        if len(list) % int(n) == 0:
            num_of_line = int(len(list) / int(n))
        else:
            num_of_line = int(len(list) / int(n)) + 1
        print(num_of_line)
        num_of_file = 1
        write_file = open(write_file_name_head + str(num_of_file) + ".txt", "w")
        for i, line in enumerate(list):
            print(line.replace("\n", ""))
            write_file.write(line.replace("\n", ""))
            write_file.write("\n")
            if int(i % num_of_line) == num_of_line - 1 and num_of_file + 1 <= n:
                write_file.close()
                num_of_file += 1
                write_file = open(write_file_name_head + str(num_of_file) + ".txt", "w")
        write_file.close()




if __name__ == "__main__":
    # num = input("input number:")
    # file_name = input("input file name:")
    # write_file_name_head = input("input write file name head:")
    # split_file(write_file_name_head, file_name, num)
    split_file("py16_out", "hightemp.txt", 5)

# oku-dhcp19:pyknock satosato$ split -l 6 hightemp.txt py16_sp
#->py16_spaa,ab,ac,ad