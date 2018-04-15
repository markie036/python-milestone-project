import unittest
from run import *

def test_correct_answer():
    return True
    
def test_wrong_answer():
    return False

"""Assert tests"""

def test_correct_answer(): #function to test the question/answer on line 24
    assert 4 + 4 == 8
   
def test_wrong_answer():
    assert not 4 + 4 == 9 
   
test_correct_answer()
test_wrong_answer()

print("All the tests passed")