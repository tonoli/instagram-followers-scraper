def numbers(found, expected):
    print('Number of users: %i' % found)
    if found < expected:
        mean_users = expected - found
        print(
            """Expected {} users but only found {}. {} {} probably blocked
            you.""".format(
                expected,
                found,
                mean_users,
                'people' if mean_users != 1 else 'person'
            )
        )


def diff(current = [], previous = []):
    new_users = list(set(current) - set(previous))
    lost_users = list(set(previous) - set(current))
    new_length = len(new_users)
    lost_length = len(lost_users)

    def print_users(users, lost=False):
        print('{} {} user{}:'.format(
            len(users),
            'removed' if lost else 'new',
            's' if len(users) != 1 else '')
        )
        for user in users:
            print(user)

    if (new_length + lost_length) > 0:
        print('\n' + '-' * 10 + '\n')
        if (new_length is not 0):
            print_users(new_users)
        if (lost_length is not 0):
            print_users(lost_users, True)
