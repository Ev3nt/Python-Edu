import math

# Принимает строку, возвращает список из мощности алфавита, энтропии Хартли, Шеннона и избыточности.
def CalcEntropy(str):
    str = str.lower()

    size = len(str)
    print(size)
    letters = set(str)
    power = len(letters)
    Hartly = math.log2(power)
    Shennon = 0
        
    for l in letters:
        count = str.count(l)
        percent = count / size

        if percent == 0:
            continue

        Shennon -= percent * math.log2(percent)

    redundancy = (Hartly - Shennon) / Hartly * 100

    return [power, Hartly, Shennon, redundancy]