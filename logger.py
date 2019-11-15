# logger test

from datetime import datetime
import logging

now = datetime.now().date()

logging.basicConfig(
    filename='log-{}.log'.format(now),
    filemode='w',
    format='%(asctime)s %(message)s'
    )

logger = logging.getLogger()


#Test messages 
logger.debug("Harmless debug Message") 
logger.info("Just an information") 
logger.warning("Its a Warning") 
logger.error("Did you try to divide by zero") 
logger.critical("Internet is down") 