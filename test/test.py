# The Scripts is to test the helper.py

''' Set up for importing file'''
import os
import sys
import pytest
import platform
import logging
sys.path.append(os.getcwd())

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.helper import display_name, display_greeting, say_hello
from libraries.operation import add_num, sub_num, div_num, mul_num, odd_even
from libraries.osinformation import find_os_path_separator
from libraries.sociallife import find_friend_surname
from libraries import sociallife
from libraries.sociallife import mod_info_dict, del_info_dict

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_display_name():
    ''' This test is check display name function'''
    user_name = "Ajeya"
    expected_value = "Your name is Ajeya"
    logger.debug(f"Input value is {user_name}")
    logger.debug(f"Expected value is {expected_value}")
    actual_value = display_name(user_name)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == display_name(user_name)

def test_display_greeting():
    ''' This test is check display greeting function'''
    expected_value = "Welcome to India"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = display_greeting()
    logger.debug(f"Actual value is {actual_value}")
    assert expected_value == display_greeting()

def test_base_file(capsys):
    "to check greetings"
    say_hello()
    out,err = capsys.readouterr()
    expected_value = "Hello World\n"
    assert out == expected_value
    assert err ==""

def test_add_num():
    ''' to test add_num function in libraries.operation file'''
    logger.info('test to add two integer')
    num_1 = 4
    num_2 = 5
    logger.debug(f"Input value 1 is {num_1}")
    logger.debug(f"Input value 1 is {num_2}")
    expected_value = 9
    logger.debug(f"Expected value is {expected_value}")
    actual_value = add_num(num_1, num_2)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == add_num(num_1, num_2)

def test_sub_num():
    ''' to test sub_num function in libraries.operation file'''
    logger.info('test to subtract two integer')
    num_3 = 12
    num_4 = 3
    logger.debug(f"Input value 1 is {num_3}")
    logger.debug(f"Input value 1 is {num_4}")
    expected_value = 9
    logger.debug(f"Expected value is {expected_value}")
    actual_value = sub_num(num_3, num_4)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == sub_num(num_3, num_4)

def test_mul_num():
    ''' to test mul_num function in libraries.operation file'''
    try:
        mul_num(10, 8)
    except Exception as exc:
        pytest.fail(f"Test is failed due to {exc}")

@pytest.mark.parametrize("num_7, num_8, expected_value",[(9, 2, 4.5), (15, 0, None)])
def test_div_num(num_7, num_8, expected_value):
    ''' to test div_num function in libraries.operation file'''
    logger.info(' test to check division of two numbers ')
    logger.debug(f"Input value 1 is {num_7}")
    logger.debug(f"Input value 1 is {num_8}")
    logger.debug(f"Expected value is {expected_value}")
    actual_value = div_num(num_7, num_8)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == div_num(num_7, num_8)

@pytest.mark.parametrize("num_11, expected_value",[(4, "even"),(7, "odd")])
def test_odd_even(num_11, expected_value):
    ''' to test odd_even function in libraries.operation file'''
    logger.info(' test to check whether number is odd or even')
    logger.debug(f"Input value 1 is {num_11}")
    logger.debug(f"Expected value is {expected_value}")
    actual_value = odd_even(num_11)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == odd_even(num_11)

def test_find_os_path_separator(monkeypatch):
    ''' this function is to check the os information'''
    logger.info('this function is to check the os information')
    monkeypatch.setattr(platform, "system", lambda : "Linux")
    expected_value = "/"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_os_path_separator()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_os_path_separator()

def test_find_windows_path_separator(monkeypatch):
    ''' this function is to check the os information'''
    logger.info('this function is to check the os information')
    monkeypatch.setattr(platform, "system", lambda : "Windows")
    expected_value = "\\"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_os_path_separator()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_os_path_separator()

def test_find_friend_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    logger.info('to find the friends surname in dict')
    monkeypatch.setattr('builtins.input', lambda prompt="":"Bharat")
    expected_value = "Pai"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_friend_surname()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_friend_surname()

def test_friend_invalid_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    logger.info('to find the friends surname in dict')
    monkeypatch.setattr('builtins.input', lambda prompt="":"Manoj")
    expected_value = False
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_friend_surname()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_friend_surname()

def test_mod_info_dict(monkeypatch):
    "to check dictionary with values"
    monkeypatch.setitem(sociallife.PERSON_INFO, "Name", "Akash")
    monkeypatch.setitem(sociallife.PERSON_INFO, "Surname", "Sharma")
    expected_value = "Name=Akash; Surname=Sharma;"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = mod_info_dict()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == mod_info_dict()

def test_missing_user(monkeypatch):
    "to check dictionary after deleting key values"
    monkeypatch.delitem(sociallife.PERSON_DET, "Name", raising=False)

    with pytest.raises(KeyError):
        _ = del_info_dict()
