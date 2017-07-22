from modules import file_io
from modules import stats

from modules.scraper import Scraper
from modules.utils import ask_input, ask_multiple_option


groups = ['followers', 'following']

# Ask for input
target = ask_input('Enter the target username: ')
group = ask_multiple_option(options = groups + ['both']);
print('\nEnter your Instagram credentials')
username = ask_input('Username: ')
password = ask_input(is_password = True)

def scrape(group):
    scraper = Scraper(target)
    scraper.authenticate(username, password)
    users = scraper.get_users(group, verbose = True)
    file_io.store(target, group, users)
    scraper.close()

    # Stats
    stats.numbers(len(users), scraper.expected_number)
    stats.diff(users, file_io.read_last(target, group))

if (group == 'both'):
    for group in groups:
        scrape(group)
else:
    scrape(group)
