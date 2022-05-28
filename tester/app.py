import logging
import time

from tester import config
from tester.watcher import get_number

logger = logging.getLogger(__name__)


def run():
    start = time.perf_counter()
    for image in config.BASE_IMAGES.iterdir():
        number = get_number(image)
        logger.info(number)
    delta_time = time.perf_counter() - start
    logger.info(f'Потребовалось: {delta_time:.2f}s')
