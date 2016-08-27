import requests

from radprint import radprint


def speak(animal):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    response = requests.get(
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = response.text
    radprint('The {0} says "{1}".'.format(animal, sound))


def main():
    """
    Process all animals and then print a sorted list of
    their sounds.
    """
    animals = ['cow', 'pig', 'chicken']
    for animal in animals:
        speak(animal)


if __name__ == '__main__':
    main()