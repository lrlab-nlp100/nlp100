#! /bin/sh

cat $1 | cut -f1 | sort | uniq
