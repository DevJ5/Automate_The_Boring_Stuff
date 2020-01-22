import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

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

logging.debug('End of program')
