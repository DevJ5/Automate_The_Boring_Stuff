import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Save logging to file:
logging.basicConfig(filename='mylog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# To disable all lower levels use the highest level (CRITICAL)
logging.disable(logging.CRITICAL)

"""
5 levels: debug, info, warning, error, critical
"""

logging.info('Start of program')
def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is %d, total is %d' % (i, total))
    return total

print(factorial(5))

logging.info('End of program')
