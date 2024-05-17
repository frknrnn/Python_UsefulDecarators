import logging

# Logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Decorator 
def exception_logger(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error occurred in {func.__name__}: {e}")          
            return None
    return wrapper

# Test 
@exception_logger
def risky_function(x, y):
    return x / y


if __name__ == "__main__":
    risky_function(10, 0)
