def as_unicode(string):
    if isinstance(string, bytes):
        return string.decode('latin1')
    return str(string)


def as_bytes(string):
    if isinstance(string, bytes):
        return string
    return str(string).encode('latin1')
