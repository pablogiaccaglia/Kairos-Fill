# -*- coding: utf-8 -*-
"""
@author: pablo

"""


def dateParser(res):
    parsed = list(res.split("-"))

    month = int(parsed[1])
    day = int(parsed[2])

    parsedMonth = [int(x) for x in str(month)]
    parsedDay = [int(x) for x in str(day)]

    if parsedMonth[0] == 0:
        month = parsedMonth[1]
    if parsedDay[0] == 0:
        day = parsedDay[1]

    parsedResult = [month, day]
    return parsedResult
