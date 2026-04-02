import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s-%(message)s')
def add(a,b):
    try:
        result=a+b
        logging.info(f"The sum is {result}")
        return result
    except Exception as e:
        logging.error(f"Error:{e}")
        return None

def subtraction(a,b):
    try:
        result1=a-b
        logging.info(f"The sum is {result1}")
        return result
    except Exception as e:
        logging.error(f"Error:{e}")
        return None


