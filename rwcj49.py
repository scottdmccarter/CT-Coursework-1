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

def message(a):
    if type(a) == int:
        a = [a]
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
    c = list(np.mod(np.matmul(m, g), 2))
    return c

def hammingDecoder(v):
    e = np.zeros(len(v),dtype=int)
    hT = []
    for i in range(1,len(v)+1):
        hT.append(decimalToVector(i, 3))
    ehT = list(np.mod(np.matmul(v,hT), 2))
    pos = int(''.join(str(e) for e in ehT),2) - 1
    if pos >= len(v):
        return []
    e[pos] = 1
    c = (np.mod(np.matrix(e) + np.matrix(v),2).tolist())[0]
    return c

def messageFromCodeword(c):
    a = list(c)
    for i in range(2,100):
        if 2**i -1 >= len(c):
            r = i
            break
    if 2**r -1 != len(c):
        return []
    while r >= 1:
        g = 2**(r - 1) -1
        a.remove(a[g])
        r -= 1
    return a

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



import random, math
def testAll():
    assert (message([1]) == [0, 0, 1, 1])
    assert (message([0, 0, 1]) == [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0])
    assert (message([0, 1, 1, 0]) == [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0])
    assert (message([1, 1, 1, 1, 0, 1]) == [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0])

    assert (hammingEncoder([1, 1, 1]) == [])
    assert (hammingEncoder([1, 0, 0, 0]) == [1, 1, 1, 0, 0, 0, 0])
    assert (hammingEncoder([0]) == [0, 0, 0])
    assert (hammingEncoder([0, 0, 0]) == [])
    assert (hammingEncoder([0, 0, 0, 0, 0, 0]) == [])
    assert (hammingEncoder([0, 0, 1, 1]) == [1,0,0,0,0,1,1])
    assert (hammingEncoder([1,1,0,1,0,0,1,1,0,1,1]) == [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1])
    assert (hammingEncoder([1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1]) == [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1])

    assert (hammingDecoder([1, 0, 1, 1]) == [])
    assert (hammingDecoder([0, 1, 1, 0, 0, 0, 0]) == [1, 1, 1, 0, 0, 0, 0])
    assert (hammingDecoder([1, 0, 0, 0, 0, 0, 1]) == [1, 0, 0, 0, 0, 1, 1])
    assert (hammingDecoder([1, 1, 0]) == [1, 1, 1])
    assert (hammingDecoder([1, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0])
    assert (hammingDecoder([1,0,1,1,1,0,1]) == [1, 0, 1, 0, 1, 0, 1])

    assert (messageFromCodeword([1, 0, 1, 1]) == [])
    assert (messageFromCodeword([1, 1, 1, 0, 0, 0, 0]) == [1, 0, 0, 0])
    assert (messageFromCodeword([1, 0, 0, 0, 0, 1, 1]) == [0, 0, 1, 1])
    assert (messageFromCodeword([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1])
    assert (messageFromCodeword([0, 0, 0, 0]) == [])

    assert (dataFromMessage([1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == [])
    assert (dataFromMessage([1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == [])
    assert (dataFromMessage([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == [0, 1, 1, 0, 1])
    assert (dataFromMessage([0, 0, 1, 1]) == [1])
    assert (dataFromMessage([0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]) == [0, 0, 1])
    assert (dataFromMessage([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0]) == [0, 1, 1, 0])
    assert (dataFromMessage([0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]) == [1, 1, 1, 1, 0, 1])
    assert (dataFromMessage([1, 1, 1, 1]) == [])

    assert (repetitionEncoder([0], 4) == [0, 0, 0, 0])
    assert (repetitionEncoder([0], 2) == [0, 0])
    assert (repetitionEncoder([1], 4) == [1, 1, 1, 1])

    assert (repetitionDecoder([1, 1, 0, 0]) == [])
    assert (repetitionDecoder([1, 0, 0, 0]) == [0])
    assert (repetitionDecoder([0, 0, 1]) == [0])
    assert (repetitionDecoder([1, 1, 1, 1]) == [1])

    print('all tests passed')

def randomflip(data):
    #If the encoded data is invalid (empty array), there is nothing to flip
    if len(data) == 0:
        return data
    bit = random.randrange(len(data))
    data[bit] = (data[bit]+1)%2
    return data

def testdata(inp, fliprandombit=False):
    if not fliprandombit:
        assert (inp == dataFromMessage(messageFromCodeword(hammingDecoder(hammingEncoder(message(inp))))))
    else:
        assert (inp == dataFromMessage(messageFromCodeword(hammingDecoder(randomflip(hammingEncoder(message(inp)))))))


def test_up_to(n, randflip=False, step=1):
    for i in range(1,n, step):
        testdata(decimalToVector(i,math.ceil(math.log2(i))), randflip)
    print("all tests passed")
