#!/usr/bin/python3
""" UTF8 CHECKER """


def validUTF8(data: list) -> bool:
    """
    validate a dataset if its valid UTF-8
    """
    if (type(data) is not list or any(not isinstance(i, int) for i in data)):
        return False
    ByteData = [i & 0xFF for i in data]
    try:
        ByteData = bytes(ByteData)
        ByteData.decode('utf-8')
    except UnicodeDecodeError:
        return False
    return True
