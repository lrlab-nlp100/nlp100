# coding: utf-8
import argparse


def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", '-f', default="hightemp.txt", help="Select txt file.")
    parser.add_argument("--num", '-n', default=5, type=int, help="Natunal number N")
    return parser.parse_args()
