# project/app/algorithms/ackermann.py

import logging
import logging.config
import yaml
import requests


# Load logger config
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Create a custom logger
logger = logging.getLogger(__name__)


def get_entries():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

    querystring = {"drilldowns": "Nation", "measures": "Population"}

    headers = {}

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def influeaper(s, cat):
    """
    parameters:
    a = abstract of a research paper
    """

    # logger.debug(s % ("A(% d, % d)" % (m, n)))

    return {
        "data": get_entries()
    }