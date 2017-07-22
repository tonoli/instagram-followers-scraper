"""Utility functions."""

import getpass


def ask_input(prompt = '', is_password = False):
    """Keep asking for input until it's empty."""

    while True:
        answer = getpass.getpass() if is_password == True else input(prompt)
        if answer is not '':
            return answer


def ask_multiple_option(options, prefix = 'Choose between', prompt = ': '):
    """Keep asking for input until it's empty or not in range."""

    def exists(index):
        return 0 <= index < len(options)

    while True:
        print(prefix)
        for index, option in enumerate(options):
            print('  {} - {}'.format(index + 1, option))
        answer = input(prompt).strip()
        if answer is not '':
            index = int(answer) - 1
            if exists(index):
                return options[index]
