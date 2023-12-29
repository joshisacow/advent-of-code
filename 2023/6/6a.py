def solution():
    f = open("6.txt", "r")
    times = f.readline().strip().split()[1:]
    dist = f.readline().strip().split()[1:]
    times = [int(x) for x in times]
    dist = [int(x) for x in dist]
    ret = 1
    for i, time in enumerate(times):
        curr = 0
        for possible in range(time):
            newdist = (time-possible)*possible
            if newdist > dist[i]:
                curr +=1
        ret *= curr

    return ret

print(solution())