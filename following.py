from datetime import datetime
import getpass
import os
import pickle
import time

from scraper import Scraper

# Ask for input
target = input('Enter the target username: ')
print('\nEnter your Instagram credentials')
credentials = {
    'username': input('Username: '),
    'password': getpass.getpass()
}

scraper = Scraper(target)
scraper.authenticate(credentials['username'], credentials['password'])
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


