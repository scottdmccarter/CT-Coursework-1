import numpy as np


def hammingGeneratorMatrix(r):
    """
    Hamming Generator Matrix

    :param r: a number
    :return G: the generator matrix of the (2^r-1,2^r-r-1) Hamming code
    """

    n = 2 ** r - 1

    # construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2 ** (r - i - 1))
    for j in range(1, r):
        for k in range(2 ** j + 1, 2 ** (j + 1)):
            pi.append(k)

    # construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i + 1))

    # construct H'
    H = []
    for i in range(r, n):
        H.append(decimalToVector(pi[i], r))

    # construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n - r):
        GG.append(decimalToVector(2 ** (n - r - i - 1), n - r))

    # apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    # transpose
    G = [list(i) for i in zip(*G)]

    return G


def decimalToVector(n, r):
    """
    decimalToVector
    :param n: a number s.t. n and r (0 <= n<2**r)
    :param r: a number s.t. n and r (0 <= n<2**r)
    :return v: a string v of r bits representing n
    """
    v = []
    for s in range(r):
        v.insert(0, n % 2)
        n //= 2
    return v


##############################################################

# Functions for hamming codes
# Q1
def message(a):
    """
    Converts a vector to a message for a Hamming code
    :param a: a vector of any positive length
    :return m: a message m for a Hamming code
    """
    l = len(a)
    # determines value of r by trial and error
    for i in range(2, 100):
        if 2 ** i - 2 * i - 1 >= l:
            r = i
            break
    k = 2 ** r - r - 1
    # creates output,m, first with the value of l in binary
    m = decimalToVector(l, r)
    # adds the input a to m
    m.extend(a)
    # fills out the rest of the output with zeros
    m.extend(np.zeros(k - len(m), dtype=int))
    return m


# Q2
def hammingEncoder(m):
    """
    encodes message into hamming code
    :param m: a vector of length 2**r - r - 1 for some r>= 2
    :return c: encoded message
    """
    k = len(m)
    # determines value of r by trial and error
    for i in range(2, 100):
        if 2 ** i - i - 1 >= k:
            r = i
            break
    # generates relevant generator matrix
    g = hammingGeneratorMatrix(r)
    # returns error for invalid inputs
    if k != len(g):
        return []
    # multiplies input and generator matrices to give hamming code
    c = list(np.mod(np.matmul(m, g), 2))
    return c


# Q3
def hammingDecoder(v):
    """
    Uses syndrome method to correct up to one bit error in hamming code, will return input if no error
    :param v: a vector of length 2**r -1 for some r>=2
    :return c: input with up to one bit error corrected
    """
    e = np.zeros(len(v), dtype=int)

    # Generating H^T matrix
    hT = []
    for i in range(1, len(v) + 1):
        hT.append(decimalToVector(i, len(v)))

    # multiplying e & H^T matrices to determine position of altered digit (if any)
    ehT = list(np.mod(np.matmul(v, hT), 2))
    pos = int(''.join(str(e) for e in ehT), 2)

    # if input is valid codeword, return input
    if pos == 0:
        return v
    # if input invalid return error
    if pos > len(v):
        return []
    # if input contains one error, correct error
    else:
        e[pos - 1] = 1
        c = (np.mod(np.matrix(e) + np.matrix(v), 2).tolist())[0]
        return c


# Q4
def messageFromCodeword(c):
    """
    converts hamming code into message
    :param c: vector of length 2**r -1 for some r >= 2
    :return m: a message from which the original data can be extracted
    """
    m = list(c)
    # determines value of r by trial and error
    for i in range(2, 100):
        if 2 ** i - 1 >= len(c):
            r = i
            break

    # returns error for invalid input
    if 2 ** r - 1 != len(c):
        return []

    # deletes elements with indices of form 2**(r - 1) -1
    # list iterated from end to start, avoiding errors with indices changing
    while r >= 1:
        g = 2 ** (r - 1) - 1
        del m[g]
        r -= 1
    return m


# Q5
def dataFromMessage(m):
    """
    Extracts original vector from message
    :param m: message
    :return n: original vector
    """
    k = len(m)
    # determines value of r by trial and error
    for i in range(2, 100):
        if 2 ** i - i - 1 >= k:
            r = i
            break

    # reads first part of message to determine value of l (length of original vector)
    l = int(''.join(str(e) for e in m[:r]), 2)

    # returns error for invalid inputs
    if r + l > k:
        return []

    # reads original vector from within message
    n = m[r:r + l]
    return n


# Functions for repetition codes

# Q6
def repetitionEncoder(m, n):
    """
    generates repetition code of length n
    :param m: vector of length 1, value either 1 or 0
    :param n: the length of the desired repetition code
    :return out: vector containing n elements all of value m
    """
    out = []

    # adds m to output n times
    for i in range(0, n):
        out.extend(m)
    return out


# Q7
def repetitionDecoder(v):
    """
    decodes repetition code, can correct up to (n-1)/2 errors
    :param v: repetition code
    :return: decoded message; either [1] or [0], or [] in case of error
    """
    ones = 0
    zeroes = 0

    # counts no. of zeros and ones
    for i in range(0, len(v)):
        if v[i] == 1:
            ones += 1
        elif v[i] == 0:
            zeroes += 1

    # returns 1 if more 1s than 0s in input
    if ones > zeroes:
        return [1]

    # returns 0 if more 0s than 1s in input
    elif zeroes > ones:
        return [0]

    # returns error for any other case
    else:
        return []
