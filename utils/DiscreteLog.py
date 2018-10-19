def bruteLog(b, c, m):
    s = 1;
    for i in range(m):
        s = (s* b) % m
        if s == c:
            return i + 1
    return -1



