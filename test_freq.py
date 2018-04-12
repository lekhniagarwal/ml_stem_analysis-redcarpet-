import pandas as pd

def frequency(d):
    df = pd.DataFrame(data=d)
    t_u = df['col1'].unique()
    l = len(t_u)
    freq =[]
    labels = []
    for i in range(0,l):
        x=df.loc[df['col1'] == t_u[i]]
        freq.append(len(x))
        labels.append(t_u[i])
    return freq
 

  

def test_frequency():
    a = {'col1': [1,1,1,1,2,2,2,2,3,3,4,5,5]} 
    assert frequency(a) == [4, 4, 2, 1, 2]
	

	
import pytest
@pytest.mark.parametrize("test_input , expected_output",[({'col1': [1,1,1,1,2,2,2,2,3,3,4,5,5]},[4, 4, 2, 1, 2]),({'col1': ['A','B','C','A','B']},[2,2,1]
)])

	
def test_answer(test_input , expected_output):
    result = frequency(test_input)
    assert  result == expected_output

	


		
	
