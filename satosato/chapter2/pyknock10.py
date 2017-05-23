# -*- coding: utf-8 -*-
# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

def count_num_of_line(file_name):
    c = 0
    for line in open(file_name, "r"):
        c += 1
    return c

if __name__ == "__main__":
    file_name = "hightemp.txt"
    print(count_num_of_line(file_name))


#$ wc hightemp.txt
#       24      98     813 hightemp.txt
#num of line,num of word,byte
#wc -l -> line
#wc -w -> word