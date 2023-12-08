def solution(text):
    f = open(text, "r")
    count = 0
    wordToNum = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for line in f:
        line = line.lower()
        # get first digit
        i, switch = 0, False
        while i<len(line) and not ord("0")<=ord(line[i])<=ord("9"):
            for word in wordToNum:
                if line[i:].startswith(word):
                    first = wordToNum[word]
                    switch = True
                    break
            if switch:
                break
            i+=1
        if not switch:    
            first = line[i]
        
        # get last digit
        i, switch = len(line)-1, False
        while i>=0 and not ord("0")<=ord(line[i])<=ord("9"):
            for word in wordToNum:
                if line[i:].startswith(word):
                    last = wordToNum[word]
                    switch = True
                    break
            if switch:
                break
            i-=1
        if not switch:
            last = line[i]
        count += int(first+last)
    return count


print(solution("1.txt"))