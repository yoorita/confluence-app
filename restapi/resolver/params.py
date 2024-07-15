def value(val):
    if isinstance(val, (bool, int)):
        return str(val).lower()
    elif isinstance(val, list):
        return ','.join(val)
    else:
        return val


def key(k: str):
    return k.replace("_", "-")
