import logging

logging.basicConfig(
    level=logging.INFO,
    format="| %(asctime)s | %(levelname)s | %(message)s | %(lineno)d |",
    handlers=[logging.FileHandler("system.log", encoding="utf-8"),
              logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

# this was for testing and it is working yeessssss!
# logger.info("Testing the logger")