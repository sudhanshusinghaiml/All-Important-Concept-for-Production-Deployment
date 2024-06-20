Some important magic methods (also known as dunder methods) in Python. 
These methods are used to define behaviors for objects in various contexts, such as arithmetic operations, 
comparisons, type conversions, context management, and more.

![Source](https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/)

![Source](https://nitesh-yadav.medium.com/dunder-methods-in-python-really-crazy-functions-3455ecb6472d)

### Basic Object Customization:
1. `__init__(self, ...)`: Constructor method, initializes an instance.
2. `__del__(self)`: Destructor method, cleans up when an instance is deleted.
3. `__repr__(self)`: Official string representation of an object (for developers).
4. `__str__(self)`: Informal string representation (for end-users).
5. `__format__(self, format_spec)`: Customizes string formatting using `format()`.

### Numeric and Arithmetic Operations:
6. `__add__(self, other)`: Addition (`+`).
7. `__sub__(self, other)`: Subtraction (`-`).
8. `__mul__(self, other)`: Multiplication (`*`).
9. `__truediv__(self, other)`: True division (`/`).
10. `__floordiv__(self, other)`: Floor division (`//`).
11. `__mod__(self, other)`: Modulo (`%`).
12. `__pow__(self, other[, modulo])`: Exponentiation (`**`).

### Comparison and Boolean Operations:
13. `__eq__(self, other)`: Equality (`==`).
14. `__ne__(self, other)`: Inequality (`!=`).
15. `__lt__(self, other)`: Less than (`<`).
16. `__gt__(self, other)`: Greater than (`>`).
17. `__le__(self, other)`: Less than or equal to (`<=`).
18. `__ge__(self, other)`: Greater than or equal to (`>=`).
19. `__bool__(self)`: Boolean value of an object (`bool()`).
20. `__and__(self, other)`: Bitwise AND (`&`).
21. `__or__(self, other)`: Bitwise OR (`|`).
22. `__xor__(self, other)`: Bitwise XOR (`^`).
23. `__invert__(self)`: Bitwise inversion (`~`).

### Iterable and Container Operations:
24. `__len__(self)`: Length of an object (`len()`).
25. `__getitem__(self, key)`: Indexing (`[]`).
26. `__setitem__(self, key, value)`: Setting item (`obj[key] = value`).
27. `__delitem__(self, key)`: Deleting item (`del obj[key]`).
28. `__iter__(self)`: Iterator for iteration (`iter()`).
29. `__next__(self)`: Next item in iteration (`next()`).
30. `__contains__(self, item)`: Membership test (`in`).

### Attribute Access:
31. `__getattr__(self, name)`: Accessing undefined attribute.
32. `__setattr__(self, name, value)`: Setting attribute.
33. `__delattr__(self, name)`: Deleting attribute.
34. `__dir__(self)`: Customizes `dir()` output.

### Callable Objects:
35. `__call__(self, ...)`: Making an instance callable as a function.

### Context Management:
36. `__enter__(self)`: Context manager entry point (`with` statement).
37. `__exit__(self, exc_type, exc_val, exc_tb)`: Context manager exit point.

### Type Conversion:
38. `__str__(self)`: String representation (`str()`).
39. `__repr__(self)`: Detailed string representation (`repr()`).
40. `__bytes__(self)`: Byte representation (`bytes()`).
41. `__format__(self, format_spec)`: Custom formatting (`format()`).
42. `__int__(self)`: Integer conversion (`int()`).
43. `__float__(self)`: Float conversion (`float()`).
44. `__complex__(self)`: Complex number conversion (`complex()`).

### Miscellaneous:
45. `__hash__(self)`: Custom hash value (`hash()`).
46. `__copy__(self)`: Shallow copy (`copy.copy()`).
47. `__deepcopy__(self, memo)`: Deep copy (`copy.deepcopy()`).
48. `__subclasshook__(cls, subclass)`: Customizes `issubclass()`.

### Special Methods for Contextlib and functools:
49. `__enter__`
50. `__exit__`

These magic methods allow you to define how your objects behave in various contexts and operations in Python, making them powerful tools for customizing and extending the language's capabilities.


# Examples for magic methods

### Initialization and Cleanup:
1. `__init__(self, ...)`: Constructor method, initializes an instance.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
print(obj.value)  # Output: 42
```

2. `__del__(self)`: Destructor method, cleans up when an instance is deleted.

```python
class MyClass:
    def __del__(self):
        print("Destructor called")

obj = MyClass()
del obj  # Output: "Destructor called"
```

### Representation:
3. `__repr__(self)`: Official string representation of an object (for developers).

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(repr(p))  # Output: Point(x=3, y=4)
```

4. `__str__(self)`: Informal string representation (for end-users).

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(str(p))  # Output: (3, 4)
```

### Numeric Operations:
5. `__add__(self, other)`: Addition (`+`).

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result.x, result.y)  # Output: 4 6
```

### Comparison:
6. `__eq__(self, other)`: Equality (`==`).

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # Output: True
```

### Context Management:
7. `__enter__(self)` and `__exit__(self, exc_type, exc_val, exc_tb)`: Context manager entry and exit.

```python
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using FileOpener as a context manager
with FileOpener('example.txt', 'w') as f:
    f.write('Hello, World!')
```

### Iterable and Container Operations:
8. `__len__(self)`: Length of an object (`len()`).

```python
class MyList:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5
```

### Attribute Access:
9. `__getattr__(self, name)`: Accessing undefined attribute.

```python
class MyClass:
    def __getattr__(self, name):
        return f"Attribute {name} not found"

obj = MyClass()
print(obj.some_attribute)  # Output: "Attribute some_attribute not found"
```

### Callable Objects:
10. `__call__(self, ...)`: Making an instance callable as a function.

```python
class Adder:
    def __init__(self, base):
        self.base = base
    
    def __call__(self, x):
        return self.base + x

adder = Adder(10)
result = adder(5)
print(result)  # Output: 15
```


### Miscellaneous

11. `__copy__(self)` - Shallow Copy

The `__copy__` method allows an object to define how it should be shallow copied using the `copy.copy()` function or the `copy` module.

```python
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __copy__(self):
        # Create a new instance with shallow copies of attributes
        return Point(self.x, self.y)

# Creating an instance of Point
p1 = Point(3, 4)

# Shallow copying p1 using copy.copy()
p2 = copy.copy(p1)

# Modify p2
p2.x = 10

# Check p1 and p2
print(p1.x, p1.y)  # Output: 3 4
print(p2.x, p2.y)  # Output: 10 4 (p2's x is modified, p1 remains unchanged)
```


12. `__deepcopy__(self, memo)` - Deep Copy

The `__deepcopy__` method allows an object to define how it should be deep copied using the `copy.deepcopy()` function or the `copy` module.

```python
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __deepcopy__(self, memo):
        # Create a new instance with deep copies of attributes
        new_point = Point(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))
        memo[id(self)] = new_point  # Store the new instance in the memo dictionary
        return new_point

# Creating an instance of Point
p1 = Point(3, 4)

# Deep copying p1 using copy.deepcopy()
p2 = copy.deepcopy(p1)

# Modify p2
p2.x = 10

# Check p1 and p2
print(p1.x, p1.y)  # Output: 3 4
print(p2.x, p2.y)  # Output: 10 4 (p2's x is modified, p1 remains unchanged)
```

### Explanation:
- **Shallow Copy (`__copy__`)**: The `__copy__` method defines how to create a shallow copy of the object. Shallow copying creates a new instance of the object and inserts references to the same objects found in the original.
  
- **Deep Copy (`__deepcopy__`)**: The `__deepcopy__` method defines how to create a deep copy of the object. Deep copying creates a new instance of the object and recursively inserts deep copies of nested objects, ensuring that the copied object is fully independent of the original.