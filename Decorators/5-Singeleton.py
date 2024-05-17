def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class MySingletonClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(f'Value: {self.value}')


instance1 = MySingletonClass(10)
instance2 = MySingletonClass(20)

instance1.display_value()  # Output: Value: 10
instance2.display_value()  # Output: Value: 10

print(instance1 is instance2)  # Output: True
