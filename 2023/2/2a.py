def solution(text):
    f = open(text, "r")
    possible = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    ret = 0
    for line in f:
        pre = line.strip().split(":")
        sets = pre[1].split(";")
        valid = True
        for set in sets:
            vals = set.split(",")
            curr = possible.copy()
            for val in vals:
                non, count, color = val.split(" ")
                if curr.get(color,0)<int(count):
                    valid = False
                    break
                curr[color] = curr.get(color, 0) - int(count)

            if not valid:
                break
        if not valid:
            continue
        num = pre[0].split(" ")[-1]
        ret += int(num)
    return ret

print(solution("2.txt"))
