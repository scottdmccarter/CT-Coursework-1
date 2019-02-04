import numpy as np
#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code


def hammingGeneratorMatrix(r):
    n = 2**r-1

    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose
    G = [list(i) for i in zip(*G)]

    return G


#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n
def decimalToVector(n,r):
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v


# a = [0,1,1,0,1]

def message(a):
    l = len(a)
    for i in range(2,100):
        if 2**i - 2*i -1 >= l:
            r = i
            break
    k = 2**r - r - 1
    out = decimalToVector(l, r)
    out.extend(a)
    out.extend(np.zeros(k-len(out),dtype=int))
    return out

def hammingEncoder(m):
    k = len(m)
    for i in range(2,100):
        if 2**i - i -1 >= k:
            r = i
            break
    g = hammingGeneratorMatrix(r)
    if k != len(g):
        return []
    encoded = list(np.mod(np.matmul(m, g),2))
    return encoded

def hammingDecoder(v):
    return []

def messageFromCodeword(c):
    return []

def dataFromMessage(m):
    k = len(m)
    for i in range(2,100):
        if 2**i - i -1 >= k:
            r = i
            break
    l = int(''.join(str(e) for e in m[:r]),2)
    if r+l > k:
        return []
    n = m[r:r+l]
    return n


def repetitionEncoder(m,n):
    out = []
    for i in range(0,n):
        out.extend(m)
    return out

def repetitionDecoder(v):
    ones = 0
    zeroes = 0
    for i in range(0,len(v)):
        if v[i] == 1:
            ones += 1
        elif v[i] == 0:
            zeroes += 1
    if ones > zeroes:
        return [1]
    elif zeroes > ones:
        return [0]
    else:
        return []
