from fizzbuzz import fun_fizzbuzz

def testFizzBuzz():
    assert fun_fizzbuzz(2) == '2'
    assert fun_fizzbuzz(3) == 'Fizz'
    assert fun_fizzbuzz(4) == '4'
    assert fun_fizzbuzz(5) == 'Buzz'
    assert fun_fizzbuzz(15) == 'FizzBuzz'
