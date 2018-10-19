def gcd(m,n):
    while(n):
        m, n = n, m % n
    return m

def gcdLoop(mod):
    for i in range(mod):
        print("i = " + str(i) + "\n")
        print(str(gcd(i, mod)) + "\n\n")
