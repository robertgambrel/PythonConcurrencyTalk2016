"""
Example of delegation to a subgenerator using
"yield from" syntax introduced in PEP380 (2009)
"""


def countdown(counter):
    """
    This countdown generator can be reset/changed by sending
    a new integer.
    """
    while counter > 0:
        new_value = yield counter
        if new_value is not None:
            counter = new_value
        counter = counter - 1

    # this is the only new part
    # if you send 'fault' once you're at this part, it'll restart the footrace() gen
    yield from footrace()


def footrace():
    """
    The footrace generator will start over if it is sent
    a string 'fault'
    """
    started = False
    while not started:
        status = yield 'On your marks.'
        if status == 'fault':
            continue
        status = yield 'Set.'
        if status == 'fault':
            continue
        yield 'Go!'
        started = True
