#! /usr/bin/python3
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--help',action= help)
parser.add_argument('-l',action= reading)
parser.add_argument('-a',action= writting)
parser.add_argument('-c',action= delete)
parser.add_argument('-s --max', action= maximum)
parser.add_argument('-s --min', action = minimum)
parser.add_argument('-s --moy' action= average)
parser.add_argument('-s --sum' action = total)
parser.add_argument('-t' action = ascending order)
parser.add_argument('-t --desc' action = descending order)
args = parser.parse_args()


if args.l:
    with open('board.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            print(' , '.join(row))   
    
if args.a:
    with open('board.csv') as csvfile:
         for numbers in args.a:
            csvfile.write(numbers+';')

if args.c:
    with open('board.csv') as csv file:
        csvfile.close()
