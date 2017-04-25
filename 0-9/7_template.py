#  07. テンプレートによる文生成


def make_sentence_from_template(x, y, z):
    return str(x) + '時の' + str(y) + 'は' + str(z)

print(make_sentence_from_template(12, '気温', '22.4'))