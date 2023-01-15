import pytest
from check import Test

inp_list = ['junk.txt', 'junk2.txt', 'junk3.txt']


@pytest.fixture(params=inp_list)
def setup(request):
    retVal=request.param
    # print("value = {}\n".format(retVal))
    return retVal

def test_create(setup):
    ob = Test()
    ob.create(setup)

def test_delete(setup):
    ob = Test()
    ob.check(setup)
