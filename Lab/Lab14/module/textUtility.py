from typing import Tuple
def most_word(address : str) -> Tuple[str,int] :
    file = open(address)
    most = {}
    for line in file.readlines() :
        for text in line.split() :
            if text.lower() not in most :
                most[text.lower()] = 1 
            else :
                most[text.lower()] += 1
    mostWord = ""
    Max = float('-inf')
    for key,value in most.items() :
        if value > Max :
            Max = value
            mostWord = key       
    return mostWord,Max

