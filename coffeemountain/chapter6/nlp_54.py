from nlp_53 import *

def extract_lemmas(tree_root):
    elements = tree_root.findall('.//lemma')
    lemmas = []
    for element in elements:
        lemmas.append(element.text)
    return lemmas

def extract_poses(tree_root):
    elements = tree_root.findall('.//POS')
    poses = []
    for element in elements:
        poses.append(element.text)
    return poses


if __name__ == '__main__':
    with open('nlp.txt.xml') as xml_file:
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()
        words = extract_words(root)
        lemmas = extract_lemmas(root)
        poses = extract_poses(root)

        for i in range(len(words)):
            print('%s\t%s\t%s' % (words[i], lemmas[i], poses[i]))