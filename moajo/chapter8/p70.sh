#!/usr/bin/env zsh

cat rt-polaritydata/rt-polarity.pos| gsed -e "s/^/+1 /g" > rt-polaritydata/rt-polarity.pos.p70.txt
cat rt-polaritydata/rt-polarity.neg| gsed -e "s/^/-1 /g" > rt-polaritydata/rt-polarity.neg.p70.txt

cat rt-polaritydata/rt-polarity.pos.p70.txt rt-polaritydata/rt-polarity.neg.p70.txt | sort -R > p70_concat.txt

