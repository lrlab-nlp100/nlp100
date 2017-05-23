with open('col1.txt','r') as f1, open('col2.txt','r') as f2,open('mix_13.txt','w') as f3:
    for line1 in f1.readlines():
        line2=f2.readline()
        f3.write(line1.strip('\n')+' '+line2)
with open('col3.txt','r') as f1:
    print(f1.read())
