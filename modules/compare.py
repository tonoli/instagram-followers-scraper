def get_diffs(list1, list2):
    """Finds new users and lost users and returns a tuple containing them in
    this order. If there's no difference return false."""

    new = list(set(list1) - set(list2))
    lost = list(set(list2) - set(list1))

    if bool(new + lost):
        return (new, lost)
    else:
        return False
