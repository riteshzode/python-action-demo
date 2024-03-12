import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    logger.info("Token not available!")
    #raise

if __name__ == "__main__":
    # logger.info(f"Token value: {SOME_SECRET}")
    r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={SOME_SECRET}&q=Ballarpur&aqi=yes")
    if r.status_code == 200:
        data = r.json()
        logger.info(f"The temerature in {data['location']['name']} is {data['current']['temp_c']} & Sky is {data['current']['condition']['text']}.")
