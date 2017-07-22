"""Utility functions to read and write the exports from the correct folder"""

from datetime import datetime
import glob
import ntpath
import os
import pickle
import time


def _get_directory(username):
    return 'exports/{}'.format(username)

def _write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok = True)
    try:
        pickle.dump(data, open(path, 'wb'))
        return True
    except:
        return False


def _read(path):
    with (open(path, 'rb')) as file:
        try:
            return pickle.load(file)
        except:
            return False


def store(username, group, usersList):
    """Store the scraped users list into a folder named as the username"""

    date = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')
    path = '{}/{}{}.pkl'.format(_get_directory(username), group, date)
    return _write(path, usersList)


def read_last(username, group, before_last=0):
    """Read the last file stored for a specific username"""

    files = glob.glob('{}/*.pkl'.format(_get_directory(username)))
    group_files = list(
        filter(lambda path: group in ntpath.basename(path), files))
    return _read(group_files[-1 - before_last])
