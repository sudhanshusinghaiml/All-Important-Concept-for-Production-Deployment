Certainly! Decorators in Python are a powerful tool used to modify or extend the behavior of functions or methods without permanently modifying the function itself. Here are some commonly used decorators in Python:

1. **`@classmethod`**:
   - Converts a method into a class method, where the method receives the class itself as the first argument (`cls`) instead of an instance.

2. **`@staticmethod`**:
   - Converts a method into a static method, which does not receive the instance (`self`) or the class (`cls`) as the first argument. It behaves like a regular function.

3. **`@property`**:
   - Defines a method as a property of a class, allowing you to define getters, setters, and deleters for attributes, making them behave like built-in properties.

4. **`@abstractmethod`** (from `abc` module):
   - Marks a method as abstract, which must be implemented by subclasses. Classes containing abstract methods cannot be instantiated unless all abstract methods have been overridden.

5. **`@wraps`** (from `functools` module):
   - Used to preserve the metadata of the original function when creating decorators. It ensures that the wrapper function retains the name, docstring, and other attributes of the decorated function.

6. **`@lru_cache`** (from `functools` module):
   - Implements a least-recently-used (LRU) cache for a function, storing the results of the most recent function calls with a limited size cache. Useful for optimizing functions with expensive computations.

7. **`@retry`**:
   - Retries a function call a specified number of times if it fails (raises an exception). It can be configured with parameters such as the number of retries, delay between retries, and exceptions to catch.

8. **`@contextmanager`** (from `contextlib` module):
   - Allows a function to be used as a context manager using the `with` statement. It defines a generator function that yields exactly one value to enter the context and optionally yields another value to exit the context.

9. **Custom Decorators**:
   - You can define custom decorators to add specific behaviors to functions, such as logging, input validation, authorization checks, and performance monitoring.

Certainly! Here are examples of each decorator to illustrate their usage:

1. **`@classmethod`**:

```python
class MyClass:
    class_attribute = "class attribute"

    @classmethod
    def class_method(cls):
        return cls.class_attribute

# Access class method without creating an instance
print(MyClass.class_method())  # Output: class attribute
```

In this example, `class_method` is decorated with `@classmethod`, allowing it to access and return the class attribute `class_attribute` without needing an instance of `MyClass`.

2. **`@staticmethod`**:

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Call static method directly using class name
print(MathOperations.add(3, 5))  # Output: 8
```

Here, `add` is a static method decorated with `@staticmethod`, which allows it to perform addition without needing access to the instance (`self`) or the class (`cls`).

3. **`@property`**:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

# Create an instance and use the property methods
c = Circle(5)
print(c.radius)  # Output: 5

c.radius = 10  # Setter example
print(c.radius)  # Output: 10

del c.radius  # Deleter example
```

In this example, `radius` is a property of the `Circle` class defined using `@property`, `@radius.setter`, and `@radius.deleter`. It allows controlled access to the `_radius` attribute with validation checks.

4. **`@abstractmethod`**:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Cannot instantiate Shape directly due to abstract method
# r = Shape()  # This would raise TypeError

# Instantiate and use Rectangle, which implements area method
rect = Rectangle(5, 3)
print("Area of Rectangle:", rect.area())  # Output: 15
```

In this example, `Shape` is an abstract base class with an abstract method `area`, marked with `@abstractmethod`. The `Rectangle` subclass inherits from `Shape` and implements the `area` method, allowing it to be instantiated and used.

5. **`@wraps`**:

```python
from functools import wraps

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def greet(name):
    """Greet function"""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Calling greet with args: ('Alice',), kwargs: {}
print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Greet function
```

In this example, `log_function_call` decorator wraps `func` with `@wraps(func)`, preserving metadata like function name (`__name__`) and docstring (`__doc__`). It prints function calls with arguments before executing `func`.

6. **`@lru_cache`**:

```python
from functools import lru_cache

@lru_cache(maxsize=3)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calling fibonacci function multiple times
print(fibonacci(5))  # Output: 5
print(fibonacci(10))  # Output: 55
print(fibonacci.cache_info())  # Output: CacheInfo(hits=17, misses=10, maxsize=3, currsize=3)
```

In this example, `fibonacci` function is decorated with `@lru_cache`, which caches the results of the function calls up to a maximum size (`maxsize=3`). This improves performance by avoiding redundant calculations.

7. **`@retry`** (custom decorator):

```python
import random
import time
from functools import wraps

def retry(ExceptionToCheck, tries=3, delay=1, backoff=2):
    def deco_retry(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            local_tries, local_delay = tries, delay
            while local_tries > 1:
                try:
                    return func(*args, **kwargs)
                except ExceptionToCheck:
                    time.sleep(local_delay)
                    local_tries -= 1
                    local_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return deco_retry

# Example usage:
@retry(Exception, tries=3, delay=1, backoff=2)
def unreliable_function():
    if random.randint(0, 10) < 8:
        raise Exception("An error occurred")
    return "Success"

print(unreliable_function())
```

In this custom decorator example (`@retry`), `unreliable_function` is decorated to retry the function call up to 3 times (`tries=3`) with an increasing delay (`delay=1`, `backoff=2`) if it raises an `Exception`.


8. **`@contextmanager`**

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        print(f"Opening file: {filename}")
        file = open(filename, mode)
        yield file  # This is where the execution enters the with block
    finally:
        print(f"Closing file: {filename}")
        file.close()

# Using the file_manager context manager
with file_manager('example.txt', 'w') as file:
    file.write('Hello, World!')
    # File is automatically closed at the end of the block
```


9. **Custom Decorators**:

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

In this example, `log_function_call` is a custom decorator that prints a message before and after calling the decorated function `greet`.


10. **`@cache`**
This can significantly improve performance by avoiding redundant computations. 
The @cache decorator is typically implemented using data structures like dictionaries or specialized decorators like functools.lru_cache.

Here's an example of implementing a simple @cache decorator using a dictionary

```python
def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            print(f"Cache hit for {func.__name__}{args}")
            return cached_results[args]
        else:
            print(f"Cache miss for {func.__name__}{args}")
            result = func(*args)
            cached_results[args] = result
            return result

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the fibonacci function with caching
print(fibonacci(5))  # Output: 5 (Calculates Fibonacci(5))
print(fibonacci(3))  # Output: 2 (Calculates Fibonacci(3))
print(fibonacci(5))  # Output: 5 (Uses cached result for Fibonacci(5))
```