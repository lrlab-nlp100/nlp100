import json

with open("jawiki-country.json", encoding="utf-8") as f,\
     open("text_about_england.txt", "w", encoding="utf-8") as dest:
    for line in f:
        json_dict = json.loads(line)
        if json_dict["title"] == "イギリス":
            dest.write(json_dict["text"])
            print("text was found")
            break
