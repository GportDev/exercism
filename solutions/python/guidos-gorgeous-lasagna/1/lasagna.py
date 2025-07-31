"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(actual_minutes):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    remaining_time = EXPECTED_BAKE_TIME - actual_minutes
    return remaining_time #37


def preparation_time_in_minutes(layers):
    """
    Return the time for preparate the lasagna

    This func receive the number of layers that copose the lasagna to calculate the time that will be spend
    """
    preparation = layers * PREPARATION_TIME
    return preparation #2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return the total time spended cooking

    This func receive two numbers, the number of layers of the lasagna and the time elapsed baking this
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    total_time = elapsed_bake_time + prep_time
    
    return total_time
