import logging
from pathlib import Path

from tester import config
from tester.watcher import get_number

logger = logging.getLogger(__name__)


def run():
    for image in config.BASE_IMAGES.iterdir():
        number = get_number(image)
        logger.debug(number)
