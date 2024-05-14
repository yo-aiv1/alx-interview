#!/usr/bin/python3
""" parse log file """

import sys
import re


IpC = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
DatCheck = r'\[(.*?)\]'
ReqCheck = r'"GET /projects/260 HTTP/1\.1"'
ScodeCheck = r'\d{3}'
FsizeCheck = r'\d+'

pattern = f'^({IpC}) - ({DatCheck}) {ReqCheck} ({ScodeCheck}) ({FsizeCheck})'
count = 0
FileSize = 0
StatusCodes = {"200": 0,
               "301": 0,
               "400": 0,
               "401": 0,
               "403": 0,
               "404": 0,
               "405": 0,
               "500": 0}


def PrintResult():
    """
    print result
    """
    print("File size: {}".format(FileSize))
    for key, val in StatusCodes.items():
        if val > 0:
            print("{}: {}".format(int(key), val))


try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            LineList = line.split(" ")
            if LineList[-2] in StatusCodes.keys():
                if count == 10:
                    count = 0
                    PrintResult()
                StatusCodes[LineList[-2]] = StatusCodes[LineList[-2]] + 1
                FileSize += int(LineList[-1][:-1])
                count += 1
except KeyboardInterrupt:
    PrintResult()
