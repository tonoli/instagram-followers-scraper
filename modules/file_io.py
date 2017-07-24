"""Utility functions to read and write the exports of a user."""

from datetime import datetime
import glob
import ntpath
import os
import pickle
import time


def _base_directory(username):
    """Get the directory where the file that needs to be read or written is."""

    return 'exports/{}'.format(username)


def _write(path, data):
    """Write a pickle file at a specified path. If the folder does not exist
    yet, create it."""

    os.makedirs(os.path.dirname(path), exist_ok = True)
    try:
        pickle.dump(data, open(path, 'wb'))
        return True
    except:
        return False


def _read(path):
    """Read a pickle file at a specified path."""

    with (open(path, 'rb')) as file:
        try:
            return pickle.load(file)
        except:
            return False


def store(username, group, usersList):
    """Store the scraped users list in a file saved into a folder that has the
    same name as the username."""

    date = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')
    path = '{}/{}{}.pkl'.format(_base_directory(username), group, date)
    return _write(path, usersList)


def read_last(username, group, before_last=1):
    """Read the last file that was stored for a specific username."""

    files = glob.glob('{}/*.pkl'.format(_base_directory(username)))
    group_files = list(
        filter(lambda path: group in ntpath.basename(path), files))
    try:
        return _read(group_files[-before_last])
    except:
        return False
