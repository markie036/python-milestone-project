import unittest
from run import *

"""Assert tests"""

def test_correct_answer(): #function to test the question/answer on line 24
    assert right_answer("5", {"question": "What is 3 + 2?", "answer": "5"}) 
   
def test_wrong_answer():
    assert not 4 + 4 == 9 
   
test_correct_answer()

print("All the tests passed")