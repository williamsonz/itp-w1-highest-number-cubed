"""This is the entry point of the program."""


def highest_number_cubed(limit):
    for num in range(1, 100):
        if (num ** 3) > limit:
            return (num - 1)
