def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]

def min(*args, key=None):
    return get_first_from_sorted(args, key, False)

def max(*args, key=None):
    return get_first_from_sorted(args, key, True)
