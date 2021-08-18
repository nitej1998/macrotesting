from datetime import datetime

import os
import logging
import json
import pytz

conf_file_path = str(os.getcwd()) + '\\Configuration.json'
# conf_file_path = str(os.getcwd()) + '\\localConfiguration.json'


def get_file_object(file_path):
    """ converts given file in to dictionary"""
    with open(file_path, 'r') as fo:
        path_dict = json.loads(fo.read())
    return path_dict


def get_time():
    """ returns date time as per the given time zone"""
    format = "%Y-%m-%d %H:%M:%S"
    now_utc = datetime.now(pytz.timezone('Asia/Kolkata'))
    p = datetime.strptime(now_utc.strftime(format), '%Y-%m-%d %H:%M:%S')
    return (p)


# creating config dic
config_dic = get_file_object(conf_file_path)

# -------- Logging Function --------------


def logging_handler():
    """
    Expects no parameters

    returns: logger object
    """
    log_filename = "macro_Logs_" + str(datetime.now().strftime('%d-%m-%Y')) + '.log'
    log_file_path = config_dic["LogFilePath"] + '\\' + log_filename
    log_format = '%(asctime)s- %(levelname)-8s- %(filename)s- %(funcName)s- %(lineno)s- %(message)s'

    logger = logging.getLogger()
    level = config_dic["LoggingLevel"]
    if level == "CRITICAL":
        logger.setLevel(logging.CRITICAL)
    elif level == "ERROR":
        logger.setLevel(logging.ERROR)
    elif level == "WARNING":
        logger.setLevel(logging.WARNING)
    elif level == "INFO":
        logger.setLevel(logging.INFO)
    elif level == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif level == "NOTSET":
        logger.setLevel(logging.NOTSET)
    else:
        logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(log_format, datefmt=str(get_time()))

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


logger = logging_handler()

def debug(functionname='Function name not available', filename='Function name not available', data="No input parameter", message='Message not available', **kwargs):
    """
Log a message with severity 'DEBUG' on the root logger. If the logger has
no handlers, call basicConfig() to add a console handler with a pre-defined
format.
"""
    try:
        if message is None:
            logging_string = ' {}  {}  Data: {}, '.format(str(functionname), str(filename), str(data))
            for key, value in kwargs.items():
                logging_string = logging_string + str(str(key) + ':' + str(value) + ', ')
            logger.debug(str(logging_string))
        else:
            logging_string = ' {}  {}  {}'.format(str(functionname), str(filename), str(message))
            logger.debug(str(logging_string))

    except Exception as Error:
        logger.exception('Error expected while recording log(exception mode) data: ' + str(Error))


def exception(functionname='Function name not available', filename='File name not available', data="No input parameter", **kwargs):
    """
Log a message with severity 'ERROR' on the root logger, with exception
information. If the logger has no handlers, basicConfig() is called to add
a console handler with a pre-defined format.
"""
    try:
        logging_string = ' {} {} '.format(str(functionname), str(filename))
        logger.exception(str(logging_string))
    except Exception as Error:
        logger.exception('Error expected while recording log(exception mode) data: ' + str(Error))


def info(message='Message not available'):
    """
Log a message with severity 'INFO' on the root logger. If the logger has
no handlers, call basicConfig() to add a console handler with a pre-defined
format.
"""
    try:
        logger.info(message)
    except Exception as Error:
        logger.exception('Error expected while recording log(info mode) data: ' + str(Error))


def warning(message='Message not available'):
    """
Log a message with severity 'WARNING' on the root logger. If the logger has
no handlers, call basicConfig() to add a console handler with a pre-defined
format.
"""
    try:
        logger.warning(message)
    except Exception as Error:
        logger.exception('Error expected while recording log(info mode) data: ' + str(Error))

