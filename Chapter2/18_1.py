line_file=[]
list=[]
dict={}
with open('a.txt', 'r') as f:
    for line in f:
        for word in line.strip('\n').split('\t'):
            if word:
                line_file.append(word)
        list.append(line_file)
        line_file=[]

list.sort(key=lambda x: float(x[2]), reverse=True)
print(list)