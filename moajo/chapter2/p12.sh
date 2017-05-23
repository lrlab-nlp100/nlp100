#! /bin/sh

cat $1 | cut -f1 >> col1.txt
cat $1 | cut -f2 >> col2.txt
