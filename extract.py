#!/usr/bin/env python3
""" Extract original string from XML file """

import xml.etree.ElementTree as ET
from sys import argv

argv = argv[1:]

def original_string(path, sep='|'):
    tree = ET.parse(path)
    string = ''

    for child in tree.getroot().iter():
        val = child.text.strip()
        if val:
            string += val + sep

    if string:
        string = sep + string

    return string

if __name__ == '__main__':
    if argv:
        print(original_string(argv[0]))
    else:
        print('\n\tXML path required.')
