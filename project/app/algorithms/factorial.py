
# project/app/algorithms/factorial.py

import logging
import logging.config
import yaml


# Load logger config
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Create a custom logger
logger = logging.getLogger(__name__)


def calc_factorial(n: int):
    """Returns the factorial of a number provided by the user
    0! = 1              if n=0
    n!=n*(n−1)!         if n>1
    """

    logger.debug(f"Generating Factorial for the numbers {n}!")

    factorial = 1

    # check if the number is negative, positive or zero
    if n < 0:
        logger.warning(f"User has given negative value {n}. This cannot be processed.")
        return "Please enter a positive integer"
    elif n == 0:
        logger.debug(f"User has given value {n}. Fixed result {factorial}")
        return factorial
    else:
        logger.debug(f"User has given value {n}!. Iteration started...")
        for i in range(1, n + 1):
            factorial = factorial*i
    return factorial
