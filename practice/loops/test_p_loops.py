from p_loops import digital_root, fizzbuzz, is_prime


def test_fizzbuzz():
    assert fizzbuzz(0) == []
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_is_prime():
    assert [n for n in range(30) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert is_prime(1_000_003)
    assert not is_prime(1_000_001)


def test_digital_root():
    assert digital_root(0) == 0
    assert digital_root(3300) == 6
    assert digital_root(9875) == 2
