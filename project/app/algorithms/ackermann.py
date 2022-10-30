# project/app/algorithms/ackermann.py

import logging
import logging.config
import yaml


# Load logger config
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Create a custom logger
logger = logging.getLogger(__name__)


def calc_ackermann(m, n, s="% s"):
    """computes the value of the Ackermann function for the input integers m and n.
    the Ackermann function being:
    A(m,n)=n+1               if m=0
    =A(m-1,1)          if m>0 and n=0
    =A(m-1,A(m,n-1)    if m>0 and n>0
    """

    logger.debug(s % ("A(% d, % d)" % (m, n)))

    if m == 0:
        logger.debug(f"A(0, {n}) = {n+1} | if m=0")
        return n + 1

    elif n == 0:
        logger.debug(f"A({m}, 0) = A({m-1}, 1) | if m>0 and n=0")
        return calc_ackermann(m - 1, 1, s)

    else:
        n2 = calc_ackermann(m, n - 1, s % ("A(% d, %% s)" % (m - 1)))
        return calc_ackermann(m - 1, n2, s)
