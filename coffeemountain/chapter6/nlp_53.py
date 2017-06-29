from xml.etree import ElementTree

def extract_words(tree_root):
    elements = tree_root.findall('.//word')
    words = []
    for element in elements:
        words.append(element.text)
    return words

if __name__ == '__main__':
    with open('nlp.txt.xml') as xml_file:
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()
        words = extract_words(root)
        for word in words:
            print(word)