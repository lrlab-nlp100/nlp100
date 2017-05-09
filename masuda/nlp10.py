f = open('hightemp.txt', encoding = 'utf-8')
count = 0
while f.readline() != "":
    count += 1
print(count)

# import locale
# print(locale.getpreferredencoding())
# import sys
# print(sys.getfilesystemencoding())
# print(sys.stdout.encoding)
# print(sys.getdefaultencoding())
