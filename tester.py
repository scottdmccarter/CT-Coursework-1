import random, math, rwcj49
def testAll():
    assert (rwcj49.message([1]) == [0, 0, 1, 1])
    assert (rwcj49.message([0, 0, 1]) == [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0])
    assert (rwcj49.message([0, 1, 1, 0]) == [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0])
    assert (rwcj49.message([1, 1, 1, 1, 0, 1]) == [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0])

    assert (rwcj49.hammingEncoder([1, 1, 1]) == [])
    assert (rwcj49.hammingEncoder([1, 0, 0, 0]) == [1, 1, 1, 0, 0, 0, 0])
    assert (rwcj49.hammingEncoder([0]) == [0, 0, 0])
    assert (rwcj49.hammingEncoder([0, 0, 0]) == [])
    assert (rwcj49.hammingEncoder([0, 0, 0, 0, 0, 0]) == [])
    assert (rwcj49.hammingEncoder([0, 0, 1, 1]) == [1,0,0,0,0,1,1])
    assert (rwcj49.hammingEncoder([1,1,0,1,0,0,1,1,0,1,1]) == [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1])
    assert (rwcj49.hammingEncoder([1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1]) == [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1])

    assert (rwcj49.hammingDecoder([1, 0, 1, 1]) == [])
    assert (rwcj49.hammingDecoder([0, 1, 1, 0, 0, 0, 0]) == [1, 1, 1, 0, 0, 0, 0])
    assert (rwcj49.hammingDecoder([1, 0, 0, 0, 0, 0, 1]) == [1, 0, 0, 0, 0, 1, 1])
    assert (rwcj49.hammingDecoder([1, 1, 0]) == [1, 1, 1])
    assert (rwcj49.hammingDecoder([1, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0])
    assert (rwcj49.hammingDecoder([1,0,1,1,1,0,1]) == [1, 0, 1, 0, 1, 0, 1])

    assert (rwcj49.messageFromCodeword([1, 0, 1, 1]) == [])
    assert (rwcj49.messageFromCodeword([1, 1, 1, 0, 0, 0, 0]) == [1, 0, 0, 0])
    assert (rwcj49.messageFromCodeword([1, 0, 0, 0, 0, 1, 1]) == [0, 0, 1, 1])
    assert (rwcj49.messageFromCodeword([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1])
    assert (rwcj49.messageFromCodeword([0, 0, 0, 0]) == [])

    assert (rwcj49.dataFromMessage([1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == [])
    assert (rwcj49.dataFromMessage([1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == [])
    assert (rwcj49.dataFromMessage([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == [0, 1, 1, 0, 1])
    assert (rwcj49.dataFromMessage([0, 0, 1, 1]) == [1])
    assert (rwcj49.dataFromMessage([0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]) == [0, 0, 1])
    assert (rwcj49.dataFromMessage([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0]) == [0, 1, 1, 0])
    assert (rwcj49.dataFromMessage([0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]) == [1, 1, 1, 1, 0, 1])
    assert (rwcj49.dataFromMessage([1, 1, 1, 1]) == [])

    assert (rwcj49.repetitionEncoder([0], 4) == [0, 0, 0, 0])
    assert (rwcj49.repetitionEncoder([0], 2) == [0, 0])
    assert (rwcj49.repetitionEncoder([1], 4) == [1, 1, 1, 1])

    assert (rwcj49.repetitionDecoder([1, 1, 0, 0]) == [])
    assert (rwcj49.repetitionDecoder([1, 0, 0, 0]) == [0])
    assert (rwcj49.repetitionDecoder([0, 0, 1]) == [0])
    assert (rwcj49.repetitionDecoder([1, 1, 1, 1]) == [1])

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
        assert (inp == rwcj49.dataFromMessage(rwcj49.messageFromCodeword(rwcj49.hammingDecoder(rwcj49.hammingEncoder(rwcj49.message(inp))))))
    else:
        assert (inp == rwcj49.dataFromMessage(rwcj49.messageFromCodeword(rwcj49.hammingDecoder(randomflip(rwcj49.hammingEncoder(rwcj49.message(inp)))))))


def test_up_to(n, randflip=False, step=1):
    for i in range(1,n, step):
        testdata(rwcj49.decimalToVector(i,math.ceil(math.log2(i))), randflip)
    print("all tests passed")
