if __name__ == "__main__":
    f = open("5.txt", "r")
    seeds = f.readline().strip().split()[1:]
    # [[start, length], ...]
    seeds = [[int(seeds[i]), int(seeds[i+1])] for i in range(0, len(seeds), 2)]
    
    changed = set()
    for line in f:
        line = line.strip()
        if line == "":
            continue
        elif line[-4:] == "map:":
            changed.clear()
            continue
        dst, src, range = line.split()
        dst, src, range = int(dst), int(src), int(range)
        for i, seed in enumerate(seeds):
            if i not in changed and src+range > seed[0] and src < seed[0]+seed[1]:
                if seed[0]+seed[1] <= src+range and seed[0] >= src:
                    # no split
                    seed[0] = dst + seed[0] - src
                elif seed[0]+seed[1] <= src+range:
                    # split new lower seed
                    seeds.append([seed[0], src-seed[0]])
                    seed[1] = seed[0]+seed[1]-src
                    seed[0] = dst
                elif seed[0] >= src:
                    # split new upper seed
                    seeds.append([src+range, seed[0]+seed[1]-src-range])
                    seed[1] = src + range - seed[0]
                    seed[0] = dst + seed[0] - src
                else:
                    # 2 splits
                    seeds.append([seed[0], src-seed[0]])
                    seeds.append([src+range, seed[0]+seed[1]-src-range])
                    seed[1] = range
                    seed[0] = dst
                changed.add(i)

    print(min([x[0] for x in seeds]))
