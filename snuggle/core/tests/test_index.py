import pytest

from ..index import Index


@pytest.fixture
def index():
    return Index()


@pytest.mark.parametrize(
        'expected, index',
        [
            ([], Index()),
            ([0, 1, 2], Index(3))
        ]
)
def test_init(expected, index):
    assert expected == index


def test_getitem_raises(index):
    with pytest.raises(IndexError):
        index[2]


def test_getitem():
    index = Index(3)
    assert index[2] == 2


def test_setitem(index):
    index[2] = 2
    assert 0 == index[2]
    assert [2] == index


def test_setitem_raises(index):
    with pytest.raises(IndexError):
        index[3] = 2


def test_setitem_unchanged():
    index = Index(2)
    index[5] = 5
    index[3] = 3
    index[1] = 1

    assert [0, 1, 5, 3] == index
