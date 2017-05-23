import re
Template={}
count=[]

pattern = re.compile(r'^\{\{基礎情報(.*?)\}\}$',re.MULTILINE + re.DOTALL)#元字符“.”在默认模式下，匹配除换行符外的所有字符。在DOTALL模式下，匹配所有字符，包括换行符

with open('uk.txt','r') as f:
    Template_content=pattern.search(f.read())
    target_Template=Template_content.group(1).split('\n')
    for line in target_Template:
        target=re.search(r'^\|(.+)\s=\s(.+)$',line)
        if target:
            Template.setdefault(target.group(1),target.group(2))
            count.append(target.group(1))


for i in count:
    print ("%s = %s" % (i, Template[i]))