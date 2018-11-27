#!/usr/local/bin/python
# coding: utf-8


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
    https://github.com/ddnet/ddnet-scripts/blob/203fcb4241261ae8f006362303723e4546e0e7f7/servers/scripts/ddnet.py#L177

    :type name: str
    :return:
    """
    try:
        n = u''
        t = 0
        i = 0

        for c in name:
            if t == 0:
                if c == '-':
                    t = 1
                else:
                    n += c
            else:
                if c == '-':
                    n += chr(i)
                    t = 0
                    i = 0
                else:
                    i = i * 10 + int(c)
        return n.encode('utf-8')
    except UnicodeEncodeError:
        return name.encode('utf-8')
