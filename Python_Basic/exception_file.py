import logging
logging.basicConfig(filename="error.log",level=logging.ERROR)
try:
    10/0
except ZeroDivisionError as e:
    logging.error("i am trying to heldle a zerodivision error {}".format(e))
