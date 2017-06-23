import json

with open("jawiki-country.json", "r", encoding="utf8") as f, open("england.txt", "w",encoding="utf8") as g:
    json_data = f.readline()
    
    while json_data:
        line = json.loads(json_data)
        if line["title"] == "イギリス":
            g.write(line["text"])
        json_data = f.readline()