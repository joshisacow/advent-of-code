def solution(text):
    f = open(text, "r")
    zero = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    ret = 0
    for line in f:
        pre = line.strip().split(":")
        sets = pre[1].split(";")

        minCount = zero.copy()        
        for set in sets:
            vals = set.split(",")

            curr = zero.copy()
            for val in vals:
                # count cubes
                non, count, color = val.split(" ")
                curr[color] = curr.get(color, 0) + int(count)
            
            # find min counts  of cubes
            for color in curr:
                minCount[color] = max(minCount[color], curr[color])

        # find power of min set
        power = 1
        for val in minCount.values():
            power*=val
        ret += power
    return ret

print(solution("2.txt"))
