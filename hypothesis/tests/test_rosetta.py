from hypothesis import given, example
from hypothesis.strategies import text
from src.rosetta_code import decode, encode


@given(text())
@example("")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
