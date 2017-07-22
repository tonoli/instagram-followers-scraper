import file_io
import stats

from scraper import Scraper
from utils import ask_input, ask_multiple_option


# Ask for input
target = ask_input('Enter the target username: ')
group = ask_multiple_option(options = ['followers', 'following']);
print('\nEnter your Instagram credentials')
username = ask_input('Username: ')
password = ask_input(is_password = True)

# Start scraping
scraper = Scraper(target)
scraper.authenticate(username, password)
users = scraper.get_users(group, verbose = True)
file_io.store(target, group, users)
scraper.close()

# Stats
stats.numbers(len(users), scraper.expected_number)
stats.diff(users, file_io.read_last(username, group))
