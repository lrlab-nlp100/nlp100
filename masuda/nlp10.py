f = open('hightemp.txt', encoding = 'utf-8')
count = 0
while f.readline() != "":
    count += 1
print(count)

# wc hightemp.txt

# import locale
# print(locale.getpreferredencoding()) (cp932)
# export PYTHONIOENCODING="utf-8" で標準出力は変更可能?(改行コード以外)
# import sys
# print(sys.getfilesystemencoding())
# print(sys.stdout.encoding)
# print(sys.getdefaultencoding())
