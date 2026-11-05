from l22_exercises import (
    approx_equal,
    machine_epsilon,
    max_unsigned,
    to_base,
    to_signed,
    total_cents,
    utf8_bytes,
    utf8_length,
    wrap,
)


def test_max_unsigned():
    assert max_unsigned(1) == 1
    assert max_unsigned(8) == 255
    assert max_unsigned(32) == 4_294_967_295


def test_utf8_bytes():
    assert utf8_bytes("") == 0
    assert utf8_bytes("abc") == 3
    assert utf8_bytes("café") == 5
    assert utf8_bytes("🐍") == 4


def test_to_base():
    assert to_base(0, 2) == "0"
    assert to_base(13, 2) == "1101"
    assert to_base(255, 2) == "11111111"
    assert to_base(64, 8) == "100"
    assert to_base(3300, 10) == "3300"


def test_wrap():
    assert wrap(260, 8) == 4
    assert wrap(255, 8) == 255
    assert wrap(-1, 8) == 255
    assert wrap(2**32, 32) == 0


def test_to_signed():
    assert to_signed(0, 8) == 0
    assert to_signed(127, 8) == 127
    assert to_signed(128, 8) == -128
    assert to_signed(255, 8) == -1
    assert to_signed(2**31, 32) == -(2**31)


def test_approx_equal():
    assert approx_equal(0.1 + 0.2, 0.3)
    assert approx_equal(0.0, 0.0)
    assert not approx_equal(1.0, 1.1)
    assert approx_equal(1e16, 1e16 + 2)
    assert approx_equal(100.0, 101.0, rel_tol=0.01)
    assert not approx_equal(100.0, 102.0, rel_tol=0.01)


def test_total_cents():
    assert total_cents([]) == 0
    assert total_cents([0.1, 0.2]) == 30
    assert total_cents([1.15]) == 115
    assert total_cents([19.99, 0.01]) == 2000


def test_machine_epsilon():
    eps = machine_epsilon()
    assert eps == 2**-52
    assert 1.0 + eps != 1.0
    assert 1.0 + eps / 2 == 1.0


def test_utf8_length():
    for ch in ["A", "é", "€", "🐍", "߿", "ࠀ", "￿"]:
        assert utf8_length(ch) == len(ch.encode("utf-8")), ch
