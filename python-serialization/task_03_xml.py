#!/usr/bin/python3
"""
you actually need a very high IQ to understand rick and morty
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('root')
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    data = ET.tostring(root)
    with open(filename, 'wb') as xml_file:
        xml_file.write(data)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    new_dict = {}
    for el in root:
        new_dict[el.tag] = el.text
    return new_dict
