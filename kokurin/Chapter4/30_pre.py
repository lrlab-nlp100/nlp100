import MeCab

file_name='neko.txt'

with open(file_name) as data_file, \
        open('neko.txt.mecab', mode='w') as out_file:
    mecab = MeCab.Tagger()
    out_file.write(mecab.parse(data_file.read()))