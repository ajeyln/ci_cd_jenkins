import logging

'''This script will do different mathematical operations such as addition, 
Substraction,Multiplication, division of two integers 
and also it shows, whether first number is odd or even'''

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#log creation for stream
fomatter_stream = logging.Formatter('%(pathname)s:%(asctime)s:%(message)s')

stream_data = logging.StreamHandler()
stream_data.setFormatter(fomatter_stream)

logger.addHandler(stream_data)

# File handler for debug
formatter_debug = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_debug = logging.FileHandler("output\operation.log", "w+")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("output\operation.log", "w+")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("output\operation.log", "w+")
filehandler_critical.setLevel(logging.CRITICAL)
filehandler_critical.setFormatter(formatter_critical)

logger.addHandler(filehandler_critical)

def add_num(number_1,number_2):
    '''This function will add two integer numbers'''
    logger.debug('This function will add two integer numbers')
    temp = number_1 + number_2 
    return temp

def sub_num(number_1,number_2):
    '''This function will subtract two integer numbers'''
    logger.debug('This function will subtract two integer numbers')
    temp = number_1 - number_2
    return temp

def mul_num(number_1,number_2):
    '''This function will multiply two integer numbers'''
    logger.debug('This function will multiply two integer numbers')
    temp = number_1 * number_2
    return temp

def div_num(number_1,number_2):
    '''This function will divide two integer numbers'''
    logger.debug('This function will divide two integer numbers')
    if number_2 == 0 : # The condition will execute while second is zero
        return None
    else:
        temp = number_1 / number_2
        return temp

def odd_even(number_1):
    '''This function will check the given number is even or odd'''
    logger.debug('This function will check the given number is even or odd')
    if(number_1 % 2 == 0):
        return "even"
    else:
        return "odd"
