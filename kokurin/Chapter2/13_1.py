with open('col1.txt','r') as f1, open('col2.txt','r') as f2,open('13_1mix.txt','w') as f3:
    for x,y in zip(f1,f2):
        f3.write(x.strip('\n')+' '+ y)
with open('col3.txt','r') as f1:
    print(f1.read())