from xml.etree import ElementTree

def extract_persons(st_xml):
    tree = ElementTree.parse(st_xml)
    root = tree.getroot()
    persons = []
    elements = root.findall('.//token')
    for element in elements:
        if element.find('NER').text == 'PERSON':
            persons.append(element.find('word').text)
    return persons



if __name__ == '__main__':
    with open('nlp.txt.xml') as xml_file:
        persons = extract_persons(xml_file)
        for person in persons:
            print(person)