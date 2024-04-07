from typing import Tuple
sentence01 = "blue-green-red-red-blue-yellow-black-white-blue-red-green-black-black-blue"

def countColor(color : str) -> Tuple[dict,str]:
    colorList = color.split("-")
    newSentence = "-".join(sorted(colorList))
    colorDict = {}
    for i in colorList :
        if i not in colorDict :
            colorDict[i] = 1
        else :
            colorDict[i] += 1
    return {k:v for k,v in sorted(colorDict.items())},newSentence

colorNumber,newSentence = countColor(sentence01)
print("""New sentence = {}
The number of each number is '{}'""".format(newSentence,colorNumber))

