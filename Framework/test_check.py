import pytest
from check import Test

inp_list = ['junk.txt', 'junk2.txt', 'junk3.txt']


@pytest.fixture(params=inp_list)
def setup(request):
    retVal = request.param
    # print("value = {}\n".format(retVal))
    return retVal


def test_create(setup):
    ob = Test()
    res = ob.create(setup)
    assert res[1] == 0


def test_delete(setup):
    ob = Test()
    d = 0
    res = ob.check(setup, d)
    if res[3] and ob.isImmutable:
        assert setup not in res[1]
        assert res[2] == 0
    if ob.isImmutable:
        assert setup in res[1]
        assert res[2] == 1
