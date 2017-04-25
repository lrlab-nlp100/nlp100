# 13. col1.txtとcol2.txtをマージ

col1 = open("col1.txt", "r", encoding='utf-8')
col2 = open("col2.txt", "r", encoding='utf-8')
f = open('col_merged.txt', 'w', encoding='utf-8')

line1 = col1.readline()
line2 = col2.readline()

while line1 or line2:
    f.write(line1[:-1] + "   " + line2)  # 改行を取り除くためのslice
    line1 = col1.readline()
    line2 = col2.readline()

f.close()
col1.close()
col2.close()
