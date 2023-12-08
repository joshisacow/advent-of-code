def solution(text):
    f = open(text, "r")
    ret = 0
    for line in f:
        # parse input
        i = 0
        while line[i] != ":":
            i+=1
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
                if curr == 0:
                    curr = 1
                else:
                    curr *=2
        
        ret += curr

    return ret

print(solution("4.txt"))
