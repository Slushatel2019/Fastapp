import logging


logger = logging.getLogger(__name__)
logger.setLevel(10)
formatter = logging.Formatter("%(levelname)s    %(asctime)s    %(pathname)s    %(message)s",
                              style="%",
                              datefmt="%Y-%m-%d %H:%M")

console_handler = logging.StreamHandler()
console_handler.setLevel(10)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
