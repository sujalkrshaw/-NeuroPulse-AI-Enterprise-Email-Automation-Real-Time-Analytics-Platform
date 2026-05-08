import logging

# Sent Logger
sent_logger = logging.getLogger("sent_logger")
sent_logger.setLevel(logging.INFO)

sent_handler = logging.FileHandler("logs/sent.log")
sent_logger.addHandler(sent_handler)

# Failed Logger
failed_logger = logging.getLogger("failed_logger")
failed_logger.setLevel(logging.ERROR)

failed_handler = logging.FileHandler("logs/failed.log")
failed_logger.addHandler(failed_handler)