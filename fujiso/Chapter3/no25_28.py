# coding: utf-8
"""
自然言語処理100本ノック

25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ

27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ

28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

from no20 import read_json
import re


def get_tempdic(article):
    tempdic = dict()
    pattern = re.compile(r"^\|(.+?)\s=\s(.+)")
    make_compiler()
    for line in article.split("\n"):
        info = re.search(pattern, line)
        if info:
            # print(info.group(0))
            tempdic[info.group(1)] = brush_up(info.group(2))
    return tempdic


def brush_up(text):
    text = br.sub(" ", text)
    text = emp.sub("", text)                               # no26
    text = inlink.sub(r"\1", text)                         # no27
    text = ref.sub("", text)                               # no28
    text = outlink.sub(r"\1", text)                           # no28
    text = middle.sub(r"\1", text)                         # no28
    return text


def make_compiler():
    global emp, inlink, br, ref, outlink, middle
    emp = re.compile("'{2,5}")                          # 強調は'が２−５個
    inlink = re.compile("\[{2}(.+?)(\|(.+?)|)\]{2}")    # [[内部リンク|読み方]]
    br = re.compile("<br/>")
    ref = re.compile("<(.+?)>(.+)|<(.+?)>")
    outlink = re.compile("\[(.+?)\]")                   # [外部リンク]
    middle = re.compile("\{\{(.+?)\}\}")                # 中カッコを消す


if __name__ == '__main__':
    print(get_tempdic(read_json()))
