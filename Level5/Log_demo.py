import logging
logging.basicConfig(filename="log.txt",level=logging.WARNING)
print("Log Demo")
logging.debug("Log Debugging")
logging.info("Log Information")
logging.warning("Log Warning")
logging.error("Error Information")
logging.critical("Critical Information")