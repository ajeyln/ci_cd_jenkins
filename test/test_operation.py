# The Scripts is to test the operation.py

''' Set up for importing file'''
import os
import sys
path = os.getcwd() # current directory of the file
file_path = (path + r'\..\libraries') # adding current to the importing directory
sys.path.append(file_path)
print(path)
print(file_path)
for i in sys.path:
    print(i)
#pylint: disable=wrong-import-position
#pylint: disable=import-error

from operation import add_num
from operation import sub_num
from operation import div_num
from operation import mul_num
from operation import odd_even

#pylint: enable=wrong-import-position
#pylint: enable=import-error


def test_add_num():
    ''' to test add_num function in operation file'''
    num_1 = 4
    num_2 = 5
    expected_value = 9
    assert expected_value == add_num(num_1, num_2)

def test_sub_num():
    ''' to test sub_num function in operation file'''
    num_3 = 12
    num_4 = 3
    expected_value = 9
    assert expected_value == sub_num(num_3, num_4)

def test_mul_num():
    ''' to test mul_num function in operation file'''
    num_5 = 10
    num_6 = 8
    expected_value = 80
    assert expected_value == mul_num(num_5, num_6)

def test_div_num():
    ''' to test div_num function in operation file'''
    num_7 = 9
    num_8 = 2
    expected_value = 4.5
    assert expected_value == div_num(num_7, num_8)

def test_odd_even():
    ''' to test odd_even function in operation file'''
    num_9 = 4
    expected_value = 'even'
    assert expected_value == odd_even(num_9)
