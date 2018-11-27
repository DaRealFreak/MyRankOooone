#!/usr/local/bin/python
# coding: utf-8
import re


def slugify(name: str) -> str:
    """Slugify function for player names from DDNet
    https://github.com/ddnet/ddnet-scripts/blob/203fcb4241261ae8f006362303723e4546e0e7f7/servers/scripts/ddnet.py#L167

    :type name: str
    :return:
    """
    x = '[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+'
    string = ""
    for c in name:
        if c in x or ord(c) >= 128:
            string += "-%s-" % ord(c)
        else:
            string += c
        return string


def deslugify(name: str) -> bytes:
    """Deslugify function for player names from DDNet
    rewritten from:
    https://github.com/ddnet/ddnet-scripts/blob/203fcb4241261ae8f006362303723e4546e0e7f7/servers/scripts/ddnet.py#L177

    :type name: str
    :return:
    """
    for special_char in re.findall('(-([\d]+)-)', name):
        name = name.replace(special_char[0], chr(int(special_char[1])))
    return name.encode('utf-8')
