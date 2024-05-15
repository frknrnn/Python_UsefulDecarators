def try_except_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
    return wrapper

# Usage
@try_except_decorator
def bol(sayi1, sayi2):
    return sayi1 / sayi2

if __name__ == "__main__":
    print(bol(10, 0))  # Error: division by zero
    print(bol(10, 2))  # 5.0