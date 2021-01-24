''' In order to import custom files from libraries folder,
 we need to reach libraries folder from source folder'''

import os
import sys
sys.path.append(os.getcwd())
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#log creation for stream
fomatter_stream = logging.Formatter('%(pathname)s:%(asctime)s:%(message)s')

stream_data = logging.StreamHandler()
stream_data.setFormatter(fomatter_stream)

logger.addHandler(stream_data)

# File handler for debug
formatter_debug = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_debug = logging.FileHandler("output\main.log")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("output\main.log")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("output\main.log")
filehandler_critical.setLevel(logging.CRITICAL)
filehandler_critical.setFormatter(formatter_critical)

logger.addHandler(filehandler_critical)

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.operation import add_num
from libraries.operation import sub_num
from libraries.operation import mul_num
from libraries.operation import div_num
from libraries.operation import odd_even
from libraries.helper import display_name
from libraries.helper import display_greeting
from libraries.osinformation import find_os_path_separator

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def oper_num(name_2, value_1, value_2, my_str):
    ''' In order to import custom files from libraries folder,
    we need to reach libraries folder from source folder'''
    logger.info(f"The user name is {name_2}")
    logger.info(f"The first number is {value_1}")
    logger.info(f"The second number is {value_2}")
    logger.info(f"The string name is {my_str}")
    display_greeting()
    display_name(name_2)
    x = add_num(value_1,value_2)
    logger.info(f"addition of two number is {x}")
    y = sub_num(value_1,value_2)
    logger.info(f"substraction of two number is {y}")
    z = mul_num(value_1,value_2)
    logger.info(f"Multiplication of two number is {z}")
    if value_2 == 0: # The condition will execute while second is zero
        logger.critical("Zero Division error")
    else:
        division_value = div_num(value_1,value_2)
        logger.critical(division_value)
    odd_even_value = odd_even(value_2)
    logger.info(odd_even_value)
    find_os = find_os_path_separator()
    logger.info(find_os)

if __name__ == '__main__':
    logger.info("Now we are doing mathematical operations")
    if len(sys.argv) != 5:
        logger.info("$ python source\main.py <user_name> <number_1> <number_2> <string_name> ")
        sys.exit(1)
    
    user_name = str(sys.argv[1])
    number_1 = int(sys.argv[2])
    number_2 = int(sys.argv[3])
    string_name = str(sys.argv[4])
    logger.info(f"Command line argument is {sys.argv}")
    oper_num(user_name, number_1, number_2, string_name)
