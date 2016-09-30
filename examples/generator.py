"""
Example of a simple generator function (PEP 255)
"""

# generator is a function

def countdown(counter):
    while counter > 0:
        yield counter
        counter = counter - 1
