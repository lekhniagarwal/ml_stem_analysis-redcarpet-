

from sklearn import metrics
def mutual_info(labels_true,labels_pred):
   return metrics.mutual_info_score(labels_true, labels_pred)  
def test_mutual_info():
    labels_true = [0, 0,1,1,1]
    labels_pred = ['A','C','A','B','C']
    assert mutual_info(labels_true,labels_pred) == 0.11849392256130004
	
	
import pytest
@pytest.mark.parametrize("test_input1,test_input2 , expected_output",[([0, 0,1,1,1],['A','C','A','B','C'],0.11849392256130004),([0, 1,1,1,2],[1,4,3,4,2],0.9502705392332346
)])

	
def test_answer(test_input1, test_input2 , expected_output):
    result = mutual_info(test_input1,test_input2)
    assert  result == expected_output

	


	

	
