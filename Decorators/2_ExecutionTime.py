import time
def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} function execution time: {execution_time:.5f} saniye")
        return result
    return wrapper

@calculate_execution_time
def example_function(n):
    time.sleep(n)
    return "Done Example Function"

@calculate_execution_time
def example_function2():
    for i in range(3):
        time.sleep(0.5)
        print(i)
    return "Done Example Function2"

if __name__ == "__main__":
    print(example_function(3))  
    print(example_function2()) 
