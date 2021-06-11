import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')

logging.basicConfig(filename='app1.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# A simple string logged at the "warning" level
logger.warning("Your log message is here")
var=7
# A string with a variable at the "info" level
logger.info("The value of var is %s", var)

# Logging the traceback for a caught exception
try:
    #function_that_might_raise_index_error()
     while False:
         print('Catching error')
except IndexError:
    # equivalent to logger.error(msg, exc_info=True)
    logger.exception("Something bad happening")