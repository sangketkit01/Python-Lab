list_input = ["aloha", "wow", "Level", "step on no pets"]

def checkMirror(word : list[str] or str) -> str :
    revList = []
    for i in word:
        rev = i[::-1].lower()
        if i.lower() == rev:
            revList.append(i)
    print("Mirror word =", ", ".join(x for x in revList))

checkMirror(list_input)

