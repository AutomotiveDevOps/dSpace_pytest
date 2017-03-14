import pytest



def test_left():
    print("Testing Left Turn Signal")
    assert True
    
def test_right():
    print("Testing Right Turn Signal")
    assert False
    
def test_forward(appl):
    if appl.platform == "car":
        assert True
    else:
        assert False, appl.platform

def test_fail():
    with pytest.raises(ZeroDivisionError):
        1/0