def solution(text):
    f = open(text, "r")
    cardMap = {}
    for line in f:
        # parse input
        i = 0
        while line[i] != ":":
            i+=1
        card, cardNum = line[:i].split()
        cardNum = int(cardNum)
        line = line[i+1:].strip()
        win, have = line.split("|")
        win, have = win.split(" "), have.split(" ")

        # process numbers
        seen, curr = set(), 0

        for num in win:
            if num == "":
                continue
            seen.add(num)

        for num in have:
            if num == "":
                continue
            if num in seen:
                curr+=1
        cardMap[cardNum] = [i for i in range(cardNum+1, cardNum+curr+1)]
    
    # process cardnum
    ret = len(cardMap)

    def recurse(card):
        cardarr = cardMap.get(card, [])
        # print(card, cardarr)
        if not cardarr:
            return
        nonlocal ret
        for newcard in cardarr:
            ret += 1
            recurse(newcard)

    for card in cardMap:
        recurse(card)
    return ret

# slow solution, dp?
print(solution("4.txt"))
