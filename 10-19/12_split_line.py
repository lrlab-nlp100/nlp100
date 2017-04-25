# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存

f = open('hightemp.txt', 'r', encoding='utf-8')
col1 = open("col1.txt", "w", encoding='utf-8')
col2 = open("col2.txt", "w", encoding='utf-8')

for line in f:
    s = line.split()
    col1.write(s[0] + "\n")
    col2.write(s[1] + "\n")
f.close()
col1.close()
col2.close()
