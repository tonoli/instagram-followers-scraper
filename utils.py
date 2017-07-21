"""Utility functions"""

import getpass


def ask_input(message = '', is_password = False):
    answer = ''
    while answer == '':
        answer = getpass.getpass() if is_password == True else input(message)
    return answer
