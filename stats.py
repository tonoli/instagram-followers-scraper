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
    new_users = list(set(previous) - set(current))
    lost_users = list(set(current) - set(previous))
    new_length = len(new_users)
    lost_length = len(lost_users)

    def print_users(users):
        print('{} new user{}:'.format(len(users), 's' if len(users) > 0 else ''))
        for user in new_users:
            print(user)

    print('\n' + '-' * 10 + '\n')
    if (new_length is not 0):
        print_users(new_users)
    if (lost_length is not 0):
        print_users(lost_users)
