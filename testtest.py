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
