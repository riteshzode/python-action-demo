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

    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=19.852156&lon=79.352093&appid={SOME_SECRET}')
    if r.status_code == 200:
        data = r.json()
        sky_details = data["weather"][0]["description"]
        logger.info(f'Weather in ballarpur: {sky_details}')