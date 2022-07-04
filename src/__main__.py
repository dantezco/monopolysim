"""Main point of entry for running the code as a module"""

from src.log import get_logger
from src.main import main

LOGGER = get_logger(__name__)


if __name__ == "__main__":
    LOGGER.info("Starting up application")
    LOGGER.info("%s", f"{main()=}")
    LOGGER.info("Application ended")
