# package time
"""
This code creates a datetime.time object from a string.

- Is it easy to verify that it works correctly?
- Do you see any obvious errors?
- How would you modify it to be easier to read?
"""

import datetime

def createTimeFromTimestamp(timestamp: str) -> datetime.time:
    """Create a datetime.time object from a string in the form 'hh:mm:ss'.

    Args:
    timestamp - string containing a timestamp in the format 'hh:mm:ss'

    Returns:
    a datetime.time object with value equal to the timestamp

    Raises:
    ValueError if timestamp is not a string in form "hh:mm:ss"

    Example:
    >>> t = createTimeFromTimestamp("9:23:15")
    >>> type(t)
    <class 'datetime.time'>
    >>> print(t)
    09:23:15
    """
    timestamp_list = timestamp.split(":")
    if len(timestamp_list) != 3:
        raise ValueError('Timestamp must be "hh:mm:ss"')
        # if the timestamp is not valid, this may raise TypeError or ValueError
    if is_valid_time(timestamp_list):
        return datetime.time(int(timestamp_list[0]), int(timestamp_list[1]), int(timestamp_list[2]))
    raise ValueError('Timestamp is not valid"')

def is_valid_time(timestamp_list):
    return  0 <= int(timestamp_list[0]) <= 23 and 0 <= int(timestamp_list[1]) < 60 and 0 <= int(timestamp_list[2]) < 60