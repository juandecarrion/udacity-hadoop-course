#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
        import re
        words = re.findall(r"[\w']+", line[4])
        words = map(lambda x: x.lower(), words)
        # if "fantastically" in words:
        #     writer.writerow(line)

        for word in words:
            print word, '\t', line[0]


# This function allows you to test the mapper with the provided test string
def main():
    mapper()

main()
