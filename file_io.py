"""Utility functions to read and write the exports from the correct folder"""

from datetime import datetime
import os
import pickle
import time


def store(username, usersList, group):
    """Store the scraped users list into a folder named as the username"""

    date = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')
    db_path = 'exports/%s/%s%s.pkl' % (username, group, date)
    os.makedirs(os.path.dirname(db_path), exist_ok = True)
    pickle.dump(usersList, open(db_path, 'wb'))
