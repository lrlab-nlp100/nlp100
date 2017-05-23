#!/usr/bin/env bash

sort p47_corpus.txt | cut -f1 |uniq -c | sort -r > p47_uniq_a.txt
sort p47_corpus.txt | cut -f1,2 | uniq -c | sort -r > p47_uniq_b.txt
