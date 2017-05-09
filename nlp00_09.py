#!/usr/bin/env python3
# coding: utf-8

'''
Created on 2016/03/14

@author: matsunagi
'''
from collections import defaultdict
import random


def exe00():
    str00 = "stressed"
    print ("".join(str00[::-1]))


def exe01():
    str01 = "パタトクカシーー"
    print (str01[0] + str01[2] + str01[4] + str01[6])


def exe02():
    str02_1 = "パトカー" 
    str02_2 = "タクシー"
    for x, y in zip(str02_1, str02_2) :
        print (x+y, end="")
    print("")

def exe03():
    str03 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = str03.split()
    mylist = []
    for word in words :
        word = word.replace(",", "").replace(".", "")
        mylist.append(len(word))
    print(mylist)

def exe04():
    str04 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    one_chara = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    words = str04.split()
    mydic = {}
    for x, word in enumerate(words) :
        word = word.replace(",", "").replace(".", "")
        if x + 1 in one_chara :
            mydic[word[0]] = word
        else :
            mydic[word[:2]] = word
    print (mydic)

def word_ngram(sequence, n=2):
    if type(sequence) == str :
        sequence = sequence.split()
    sequence = ["<s>"] + sequence + ["</s>"]
    ngrams = []
    for x, w in enumerate(sequence) :
        if x + n > len(sequence) : break
        ngrams.append(sequence[x:x+n])
    return ngrams

def character_ngram(sequence, n=2):
    if type(sequence) == list :
        sequence = " ".join(sequence)
    ngrams = []
    for x, w in enumerate(sequence) :
        if x + n > len(sequence) : break
        elif " " in sequence[x:x+n] : continue
        ngrams.append(sequence[x:x+n])
    return ngrams
    
def exe05():    
    str05 = "I am an NLPer"
    print (word_ngram(str05, n=2))
    print (character_ngram(str05, n=2))
    
def exe06():
    str06_1 = "paraparaparadise"
    str06_2 = "paragraph"
    X = character_ngram(str06_1, 2)
    Y = character_ngram(str06_2, 2)
    sum = set(X+Y)
    product = set(X).intersection(Y)
    diff = set(X).difference(Y)
    print(sum)
    print(product)
    print(diff)
    
    print ("se" in X)
    print ("se" in Y)
    
    
def exe07(x,y,z):
    return "{0}時の{1}は{2}".format(x,y,z)

def cipher(sequence, reverse=False):
    ango = ""
    for w in sequence :
        if w.islower() :
            w = chr(219 - ord(w))
        ango += w
    return ango
         
def exe08(message):
    ango = cipher(message)
    reango = cipher(ango)
    print(ango)
    print(reango)
    
def typoglycemia(sequence):
    if type(sequence) == str :
        sequence = sequence.split()
    typoglycemiad = []
    for x in sequence :
        if len(x) > 4 :
            mid = ([y for y in x[1:-1]])
            random.shuffle(mid)
            x = x[0] + "".join(mid) + x[-1]
        typoglycemiad.append(x)
    return " ".join(typoglycemiad)
    
    
if __name__ == "__main__" :
    #exe05()
    #exe06()
    exe08("This is a HAPPY message")
    print (typoglycemia("This is a HAPPY message"))
    print (typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
