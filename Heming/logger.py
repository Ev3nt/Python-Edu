'''Logger system'''

import logging

class Logger:
    '''Logger system'''

    def __init__(self, logfile):
        logging.basicConfig(filename=logfile, level=logging.DEBUG, filemode='w', format='%(levelname)s:%(asctime)s:%(message)s')

    def error(self, text):
        '''Save error message in log file.'''
        logging.error(text)

    def info(self, text):
        '''Save warn message in log file.'''
        logging.info(text)
