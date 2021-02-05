''' In order to import custom files from libraries folder,
 we need to reach libraries folder from source folder'''

import logging
import os
import sys
sys.path.append(os.getcwd())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#log creation for stream
fomatter_stream = logging.Formatter('%(pathname)s:%(asctime)s:%(message)s')

stream_data = logging.StreamHandler()
stream_data.setFormatter(fomatter_stream)

logger.addHandler(stream_data)

# File handler for debug
formatter_debug = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_debug = logging.FileHandler("output\\main.log")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("output\\main.log")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("output\\main.log")
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
    logger.info("The user name is %s", name_2)
    logger.info("The first number is %s", value_1)
    logger.info("The second number is %s", value_2)
    logger.info("The string name is %s", my_str)
    display_greeting()
    display_name(name_2)
    num_1 = add_num(value_1,value_2)
    logger.info("addition of two number is %s", num_1)
    num_2 = sub_num(value_1,value_2)
    logger.info("substraction of two number is %s", num_2)
    num_3 = mul_num(value_1,value_2)
    logger.info("Multiplication of two number is %s", num_3)
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
        logger.info("$ python source\\main.py <USER_NAME> <number_1> <number_2> <STRING_NAME> ")
        sys.exit(1)
    USER_NAME = str(sys.argv[1])
    number_1 = int(sys.argv[2])
    number_2 = int(sys.argv[3])
    STRING_NAME = str(sys.argv[4])
    logger.info("Command line argument is %s", sys.argv)
    oper_num(USER_NAME, number_1, number_2, STRING_NAME)
