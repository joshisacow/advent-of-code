def solution():
    f = open("6.txt", "r")
    times = f.readline().strip().split()[1:]
    dist = f.readline().strip().split()[1:]
    time = int("".join(times))
    dist = int("".join(dist))
    ret = 0

    # binary search to find min and max
    l, r = 1, time
    # find min
    while l<=r:
        mid = (l+r)//2
        newdist = (time-mid)*mid
        if newdist > dist:
            r = mid-1
        else:
            l = mid+1
    minTime = mid
    l, r = 1, time
    # find min
    while l<=r:
        mid = (l+r)//2
        newdist = (time-mid)*mid
        if newdist > dist:
            l = mid+1
        else:
            r = mid-1

    return mid-minTime

print(solution())