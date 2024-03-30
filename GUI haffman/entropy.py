'''Entropy calc'''

import math

def calc_entropy(string):
    '''Calculate entropy function'''
    string = string.lower()

    size = len(string)
    letters = set(string)
    power = len(letters)
    hartly = math.log2(power)
    shennon = 0

    for l in letters:
        count = string.count(l)
        percent = count / size

        if percent == 0:
            continue

        shennon -= percent * math.log2(percent)

    redundancy = (hartly - shennon) / hartly * 100

    return [power, hartly, shennon, redundancy]
