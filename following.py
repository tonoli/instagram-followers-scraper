from datetime import datetime
import os
import pickle
import time

from scraper import Scraper
from utils import ask_input


# Ask for input
target = ask_input('Enter the target username: ')
print('\nEnter your Instagram credentials')
username = ask_input('Username: ')
password = ask_input(is_password = True)

scraper = Scraper(target)
scraper.authenticate(username, password)
users = scraper.get_users('following', verbose = True)
scraper.close()

# Store the scraped following users link
date = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')
db_path = 'exports/%s/following%s.pkl' % (target, date)
os.makedirs(os.path.dirname(db_path), exist_ok = True)
pickle.dump(users, open(db_path, 'wb'))

# Stats
print('Number of followers: %i' % len(users))
if len(users) < scraper.expected_number:
    mean_users = scraper.expected_number - len(users)
    print('Expected %i followers but only found %i. %i %s probably blocked you.'
          % (
            scraper.expected_number,
            len(users),
            mean_users,
            'people' if mean_users != 1 else 'person'
        )
    )


