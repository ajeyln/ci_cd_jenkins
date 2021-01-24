''' The script to find the  personal information'''
import sys
from io import StringIO
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

filehandler_debug = logging.FileHandler("output\sociallife.log")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("output\sociallife.log")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("output\sociallife.log")
filehandler_critical.setLevel(logging.CRITICAL)
filehandler_critical.setFormatter(formatter_critical)

logger.addHandler(filehandler_critical)

friend_info = {"Sandeep":"Prabhu",
                "Puneet":"Kumar",
                "Bharat":"Pai",
                "Sachin":"Singh",
                "Alok":"Rao" }
PERSON_INFO = {'Name':'Ajeya', "Surname" : "Nayak"}
PERSON_DET = {'Name':'Sachin', "Surname" : "Singh"}

def find_friend_surname():
    ''' to find the friends surname in dict'''
    logger.info('to find the friends surname in dict')
    friend_name = input("Enter the name:")
    logger.info(f'Friend Name is {friend_name}')
    print(friend_name)
    if friend_name in friend_info.keys():
        return friend_info[friend_name]
        logger.info(f'Friend surname is {friend_info[friend_name]}')
    else:
        return False
        logger.info(f'Friend information not found')

def mod_info_dict(config=None):
    '''to find person info'''
    logger.info("here we are finding the person info")
    return f"Name={PERSON_INFO['Name']}; Surname={PERSON_INFO['Surname']};"

def del_info_dict(config=None):
    '''to find person info'''
    logger.info("here we are finding the person info")
    return f"Name={PERSON_DET['Name']}; Surname={PERSON_DET['Surname']};"
