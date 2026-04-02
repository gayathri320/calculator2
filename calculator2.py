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
        logging.info(f"The difference is {result1}")
        return result1
    except Exception as e:
        logging.error(f"Error:{e}")
        return None

def multiplication(a,b):
    try:
        result2=a*b
        logging.info(f"The product is {result2}")
        return result2
    except Exception as e:
        logging.error(f"Error:{e}")
        return None

def division(a,b):
    try:
        result3=a/b
        logging.info(f"The quotient is {result3}")
        return result3
    except Exception as e:
        logging.error(f"Error:{e}")
        return None