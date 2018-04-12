import pandas as pd

def target(funding_2008,funding_2009):
    l = len(funding_2008)
    z=[]
    for i in range(0,l):
        diff=((funding_2009[i]-funding_2008[i])/funding_2009[i])*100
      
        if(diff>=0):
            diff=1
        else:
            diff=0
        z.append(diff)
    return z 
   
def test_target():
    a = [7.8,1.8,1.1,11.6,1.42,2]
    b = [7,1.8,1.1,13,1.347,1.961]
    assert target(a,b) == [0, 1, 1, 1, 0, 0]
	

import pytest
@pytest.mark.parametrize("test_input1,test_input2 , expected_output",[([7.8,1.8,1.1,11.6,1.42,2],[7,1.8,1.1,13,1.347,1.961],[0, 1, 1, 1, 0, 0]),([2.564,3.995,0.3,1.2025,0.237,2.505],[2.525,3.48,0.3,3.113,0.362,1.913],[0, 0, 1, 1, 1, 0]
)])

	
def test_answer(test_input1, test_input2 , expected_output):
    result = target(test_input1,test_input2)
    assert  result == expected_output

	
