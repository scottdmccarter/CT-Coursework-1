import rwcj49
def testAll():
    assert( rwcj49.message([1])            ==  [0,0,1,1] )
    assert( rwcj49.message([0,0,1])        ==  [0,0,1,1,0,0,1,0,0,0,0] )
    assert( rwcj49.message([0,1,1,0])      ==  [0,1,0,0,0,1,1,0,0,0,0] )
    assert( rwcj49.message([1,1,1,1,0,1])  ==  [0,1,1,0,1,1,1,1,0,1,0] )

    assert( rwcj49.hammingEncoder([1,1,1])    ==  [] )
    assert( rwcj49.hammingEncoder([1,0,0,0])  ==  [1,1,1,0,0,0,0] )
    assert( rwcj49.hammingEncoder([0])        ==  [0,0,0] )
    assert( rwcj49.hammingEncoder([0,0,0])    ==  [] )
    #
    # assert( rwcj49.hammingDecoder([1,0,1,1])        ==  [])
    # assert( rwcj49.hammingDecoder([0,1,1,0,0,0,0])  ==  [1,1,1,0,0,0,0] )
    # assert( rwcj49.hammingDecoder([1,0,0,0,0,0,1])  ==  [1,0,0,0,0,1,1] )
    # assert( rwcj49.hammingDecoder([1,1,0])          ==  [1,1,1])
    # assert( rwcj49.hammingDecoder([1,0,0,0,0,0,0])  ==  [0,0,0,0,0,0,0] )
    #
    # assert( rwcj49.messageFromCodeword([1,0,1,1])        ==  [] )
    # assert( rwcj49.messageFromCodeword([1,1,1,0,0,0,0])  ==  [1,0,0,0] )
    # assert( rwcj49.messageFromCodeword([1,0,0,0,0,1,1])  ==  [0,0,1,1] )
    # assert( rwcj49.messageFromCodeword([1,1,1,1,1,1,1])  ==  [1,1,1,1] )
    # assert( rwcj49.messageFromCodeword([0,0,0,0])        ==  [] )
    #
    assert( rwcj49.dataFromMessage([1,0,0,1,0,1,1,0,1,0])    ==  [] )
    assert( rwcj49.dataFromMessage([1,1,1,1,0,1,1,0,1,0,0])  ==  [] )
    assert( rwcj49.dataFromMessage([0,1,0,1,0,1,1,0,1,0,0])  ==  [0,1,1,0,1] )
    assert( rwcj49.dataFromMessage([0,0,1,1])                ==  [1] )
    assert( rwcj49.dataFromMessage([0,0,1,1,0,0,1,0,0,0,0])  ==  [0,0,1] )
    assert( rwcj49.dataFromMessage([0,1,0,0,0,1,1,0,0,0,0])  ==  [0,1,1,0] )
    assert( rwcj49.dataFromMessage([0,1,1,0,1,1,1,1,0,1,0])  ==  [1,1,1,1,0,1] )
    assert( rwcj49.dataFromMessage([1,1,1,1])                ==  [] )

    assert( rwcj49.repetitionEncoder([0],4)  ==  [0,0,0,0])
    assert( rwcj49.repetitionEncoder([0],2)  ==  [0,0])
    assert( rwcj49.repetitionEncoder([1],4)  ==  [1,1,1,1])

    assert( rwcj49.repetitionDecoder([1,1,0,0])  == [] )
    assert( rwcj49.repetitionDecoder([1,0,0,0])  == [0] )
    assert( rwcj49.repetitionDecoder([0,0,1])    == [0] )
    assert( rwcj49.repetitionDecoder([1,1,1,1])  == [1] )

    print('all tests passed')
