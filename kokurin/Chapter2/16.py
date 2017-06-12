# -*- coding: UTF-8 -*-

sets=int(input('please input a number:\n'))
sent_url=[]
filenumber=0

with open('hightemp.txt','r') as f:
    total_lines=len(f.readlines())
    lim=(1+total_lines)//sets

with open('hightemp.txt','r') as f:
    for line in f:
        sent_url.append(line)
        if len(sent_url)<lim:
            continue
        filename=str(filenumber)+'.txt'
        with open(filename,'w') as file:
            for sent in sent_url[:-1]:
                file.write(sent)
            file.write(sent_url[-1].strip())
            sent_url=[]
            filenumber+=1

print('done')