import logging

logging.basicConfig(
    filename="D:\\Selenium with Python\\Selenium_Basics\\Logging\\automation.log",
    format="%(asctime)s : %(levelname)s : %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG
)

# Info and debug does not appear in file until you add "level" argument in basicConfig
logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")

# Python threshold starts from warning
logging.warning("This is a WARNING message")
logging.error("This is a ERROR message")
logging.critical("This is a CRITICAL message")
