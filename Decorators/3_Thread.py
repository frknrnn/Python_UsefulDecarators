import threading
import time

def run_in_thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

@run_in_thread
def calculate_square(number):
    time.sleep(2)
    print(f"{number} : {number ** 2}")

@run_in_thread
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    calculate_square(5)
    greet("Furkan")


