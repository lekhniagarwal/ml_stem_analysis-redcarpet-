import pandas as pd

def label_encoding(z):
    a = {'col1': z}
    new_df = pd.DataFrame(data=a)
    t_u = new_df['col1'].unique()
    l = len(t_u)
    new_label = []
    for i in range(1,l+1):
        new_label.append(i)
    for i in range(0,l):
        new_df.iloc[list(new_df['col1'] == t_u[i]),0]= new_label[i]
    z_new = list(new_df['col1'])   
    return z_new


def test_label_encoding():
    z = ["c","b","c","a","c","c","b","b"]
    result = label_encoding(z)
    assert result == [1, 2, 1, 3, 1, 1, 2, 2]
	
	
import pytest
@pytest.mark.parametrize("test_input , expected_output",[(["c","b","c","a","c","c","b","b"],[1, 2, 1, 3, 1, 1, 2, 2]),( ["mango","egg","egg","apple","orange","apple","mango","egg"],[1, 2, 2, 3, 4, 3, 1, 2]
)])

	
def test_answer(test_input , expected_output):
    result = label_encoding(test_input)
    assert  result == expected_output

	
