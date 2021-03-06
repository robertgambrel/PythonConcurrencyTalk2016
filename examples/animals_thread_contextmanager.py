"""
This module is a threaded version of
animals.py in which the animated printing
is synchronized between threads using a simple
threading.Lock as a context manager.
A raised exception will not cause a deadlock.
"""
from threading import Thread, Lock

import requests

from radprint import radprint


def speak(animal, printlock):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    session = requests.Session()
    response = session.get(
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = response.text
    with printlock:
        if 'Moo' in sound:
            raise ValueError('Not happy about moo.')
        radprint('The {0} says "{1}".'.format(animal, sound))

    session.close()


def main():
    """
    Retrieve and print sounds for all animals.
    """
    animals = ['cow', 'pig', 'chicken']
    threads = []
    printlock = Lock()
    for animal in animals:
        worker = Thread(target=speak, args=(animal, printlock))
        threads.append(worker)
        worker.start()

    for worker in threads:
        worker.join()


if __name__ == '__main__':
    main()
