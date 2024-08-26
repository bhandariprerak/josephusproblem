import main

def test_postion_to_stand():
    assert main.position_to_stand(1024) == 1 # true
    assert main.position_to_stand(41) == 19 # true
    assert main.position_to_stand(5) == 2 # false
    
    