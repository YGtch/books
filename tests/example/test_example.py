import pytest


@pytest.mark.parametrize("a,b,c", [(1, 1, 3), (2, 3, 5)])
def test_sum(a, b, c):
    assert a + b == c


@pytest.mark.parametrize(
    "file,text", [("tests/example/data/text.txt", "Hello, world!")]
)
def test_file(file, text):
    with open(file) as data:
        assert data.read().strip() == text
