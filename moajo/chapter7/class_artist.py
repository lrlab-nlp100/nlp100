import json


class Artist:
    def __init__(self, json):
        self.json = json
        self.name = json["name"]
        self.area = self.json["area"] if "area" in self.json else None
        self.tags = self.json["tags"] if "tags" in self.json else None

    def __str__(self):
        return json.dump(self.json)

    def __repr__(self):
        return self.__str__()
