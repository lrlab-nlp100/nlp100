import re

with open("england.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
    template_dict = {}
    for line in lines:
        extract_template = re.findall("|(.*?) =", line)
        print(extract_template)
        template_dict[extract_template[0]] = extract_template[0]
    print(template_dict)