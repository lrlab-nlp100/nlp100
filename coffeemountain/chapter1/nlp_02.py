str1 = "パトカー"
str2 = "タクシー"

str = "".join(i+j for i, j in zip(str1, str2))

print(str)