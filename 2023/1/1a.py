def solution(text):
    f = open(text, "r")
    count = 0
    for line in f:
        # get first digit
        i = 0
        while i<len(line) and not ord("0")<=ord(line[i])<=ord("9"):
            i+=1
        first = line[i]
        
        # get last digit
        i = len(line)-1
        while i>=0 and not ord("0")<=ord(line[i])<=ord("9"):
            i-=1
        last = line[i]
        count += int(first+last)
    return count

print(solution("1.txt"))