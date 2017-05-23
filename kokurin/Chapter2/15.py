# -*- coding: UTF-8 -*-

n=int(input("please input\n"))

with open("hightemp.txt","r") as f:
    for line in f.readlines()[-n:]: #注意[-n:]的用法和line in f.readlines()的用法
        print(line.strip('\n'))