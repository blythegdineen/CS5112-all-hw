def get_keys(data):
    """
    Returns a list of all keys in the dictionary.
    """
    keys = []
    for key, value in data.items():
            keys.append(key)
    return keys

def get_values(data):
    """
    Returns a list of all values in the dictionary.
    """
    values = []
    for key, value in data.items():
            values.append(value)
    return values

def get_items(data):
    """
    Returns a list of all key-value pairs (tuples) in the dictionary.
    """
    return list(data.items())

def get_value(data, key, default=None):
    """
    Returns the value for the given key if it exists, otherwise returns the default value.
    """
    if key in data:
        return data[key]
    else:
        return default
