# project/app/algorithms/fibonacci.py

import logging
import logging.config
import yaml


# Load logger config
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Create a custom logger
logger = logging.getLogger(__name__)


def get_nth_fibo(nterm: int):
    """ Calculate the n-th term of a Fibonacci Number by the user
    F0 = 0              if nterm=0
    F1 = 1              if nterm=1
    Fn = Fn-2 + Fn-1    if nterm>1
    """
    logger.debug(f"Generating n-th fibinacci for the number {nterm}")
    # First two terms initialization
    n1, n2 = 0, 1
    count = 0

    # Check if the number of term is valid
    if nterm <= 0:
        logger.warning(f"User has given negative value {nterm}. Cannot be processed.")
        return "Please enter a positive integer"

    # If the term value is one, return n1
    elif nterm == 0:
        logger.debug(f"User has given value {nterm}. Fixed result {n1}")
        return n1

    # If the term value is one, return nterm
    elif nterm == 1:
        logger.debug(f"User has given value {nterm}. Fixed result {nterm}")
        return nterm

    # Iterate to fibonacci sequences
    else:
        logger.debug(f"User has given value {nterm}. Iteration started...")
        while count < nterm:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

    return n1
