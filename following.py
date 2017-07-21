from scraper import Scraper
from store import store
from utils import ask_input


# Ask for input
target = ask_input('Enter the target username: ')
print('\nEnter your Instagram credentials')
username = ask_input('Username: ')
password = ask_input(is_password = True)

scraper = Scraper(target)
scraper.authenticate(username, password)
users = scraper.get_users('following', verbose = True)
store(target, users)
scraper.close()

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


