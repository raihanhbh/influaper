# project/app/main.py

import logging
import logging.config
import yaml
from enum import Enum

from fastapi import FastAPI, HTTPException, Request, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .algorithms.fibonacci import get_nth_fibo
from .algorithms.ackermann import calc_ackermann
from .algorithms.factorial import calc_factorial
from .services.influaper import influeaper
from .cprofiler_decorator import profile


class Categories(str, Enum):
    who = "WHO"
    thirty_label = "30_Label"


app = FastAPI()


# Load logger config
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(
        f.read())
    logging.config.dictConfig(
        config)


# Create a custom logger
logger = logging.getLogger(
    __name__)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(
        f"URL: {request.url}")
    logger.error(
        f"user input: {request.path_params}")
    logger.error(
        f"status code: {status.HTTP_422_UNPROCESSABLE_ENTITY}")
    logger.error(jsonable_encoder(
        {"detail": exc.errors()}))

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {"detail": exc.errors()}),
    )


@app.get("/api/v1/service/influaper/")
@profile(sort_by='cumulative', lines_to_print=10, strip_dirs=True)
def get_factorial(s: str, category: Categories = Categories.who):
    try:
        if s is None:
            raise ValueError

        influaper = influeaper(s, category)
        logger.debug(f"Influapers are {influaper}")

        return {"result": influaper}

    except ValueError:
        logger.error(
            f"Invalid input {s}. Please enter n >= 0 ")
        raise HTTPException(
            status_code=422, detail="Invalid input. Please enter string")


@app.get("/api/v1/algorithms/fibonacci/{nterm}")
@profile(sort_by='cumulative', lines_to_print=10, strip_dirs=True)
def get_fibonacci(nterm: int):
    try:
        if nterm <= 0:
            raise ValueError

        nth_number = get_nth_fibo(
            nterm)
        logger.debug(
            f"n-th fibonacci number for the term {nterm} = {nth_number}")

        return {"result": nth_number}

    except ValueError:
        logger.error(
            f"Invalid input {nterm}. Please enter a positive integer ")
        raise HTTPException(
            status_code=422, detail="Invalid input. Please enter a positive integer")


@app.get("/api/v1/algorithms/ackermann/{m}/{n}")
@profile(sort_by='cumulative', lines_to_print=10, strip_dirs=True)
def get_ackermann(m: int, n: int):
    logger.debug(
        f"Generating Ackermann Function for the numbers A({m}, {n})")

    try:
        if m < 0 or n < 0:
            raise ValueError

        ackermann_result = calc_ackermann(
            m, n)
        logger.debug(
            f"Ackermann result for A({m}, {n}) = {ackermann_result}")

        return {"result": ackermann_result}

    except ValueError:
        logger.error(
            f"Invalid input m={m}, n={n}. Please enter m >= 0 and n >= 0 ")
        raise HTTPException(
            status_code=422, detail="Invalid input. Please enter a positive integer")


@app.get("/api/v1/algorithms/factorial/{n}")
@profile(sort_by='cumulative', lines_to_print=10, strip_dirs=True)
def get_factorial(n: int):
    try:
        if n < 0:
            raise ValueError

        n_factorial = calc_factorial(
            n)
        logger.debug(
            f"Factorial {n}! = {n_factorial}")

        return {"result": n_factorial}

    except ValueError:
        logger.error(
            f"Invalid input {n}. Please enter n >= 0 ")
        raise HTTPException(
            status_code=422, detail="Invalid input. Please enter a positive integer")


@app.get("/api/v1/heartbeat")
def check_heartbeat():
    logger.info(
        "Hit heartbeat. Health status OK")
    return {"ok"}
