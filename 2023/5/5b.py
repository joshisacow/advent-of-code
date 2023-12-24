if __name__ == "__main__":
    f = open("5.txt", "r")
    seeds = f.readline().strip().split()[1:]
    seeds = [[int(seeds[i]), int(seeds[i+1])] for i in range(0, len(seeds), 2)]
    print(seeds)

    # changed = set()
    # for line in f:
    #     line = line.strip()
    #     if line == "":
    #         continue
    #     elif line[-4:] == "map:":
    #         changed.clear()
    #         continue
    #     dst, src, range = line.split()
    #     dst, src, range = int(dst), int(src), int(range)
    #     for i, seed in enumerate(seeds):
    #         if i not in changed and src <= seed < src+range:
    #             seeds[i] = dst + seed - src
    #             changed.add(i)
        
    # print(min(seeds))
