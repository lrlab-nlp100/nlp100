text=str(input('please input:\n'))
encode=''
decode=''

def enc(i):
    if i.islower():
        x=chr(219-ord(i))  #chr 和 ord的用法
        return x
    else:
        return i

for x in text:
    encode += enc(x)

print ('Cipher text:',encode)

for x in encode:
    decode +=enc(x)
print ('Plain text:',decode)