import pytest

from verstr import verstr


@pytest.mark.parametrize('mode', ['str', 'userstr', 'interface'])
def test_simple(mode):
    assert verstr("1.0.1dev", mode) < "1.0.1beta"

