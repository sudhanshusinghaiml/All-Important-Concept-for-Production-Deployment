"""
Certainly! Context managers in Python, often used with the `with` statement, allow you to manage resources, such as opening and closing files or database connections, in a controlled way. They ensure that resources are properly initialized before the block of code starts and are cleaned up when the block exits, regardless of whether the block completes successfully or raises an exception. Here are a few examples of using context managers with `@contextmanager` from the `contextlib` module and with the `__enter__` and `__exit__` methods:
"""

### Using `@contextmanager` from `contextlib`:

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

"""
#### Explanation:
1. **`@contextmanager` decorator**:
   - `@contextmanager` is used to define a generator function (`file_manager`) that serves as a context manager.

2. **`yield` statement**:
   - The `yield` statement separates the setup and teardown code. Code before `yield` runs when entering the `with` block, and code after `yield` runs when exiting the `with` block.

3. **`try...finally` block**:
   - Ensures that the file (`file`) is closed properly even if an exception occurs during execution of the block.

4. **Using `file_manager` context manager**:
   - Inside the `with` block, `file_manager('example.txt', 'w') as file` opens `example.txt` in write mode (`'w'`), writes 'Hello, World!' to it, and then automatically closes the file when the block ends.
"""


### Using `__enter__` and `__exit__` methods:

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        self.connection = f"Connection to {self.db_name}"  # Simulate connection
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to database: {self.db_name}")
        self.connection = None  # Close connection
        if exc_type is not None:
            print(f"Exception occurred: {exc_type}, {exc_val}")

# Using DatabaseConnection as a context manager
with DatabaseConnection('my_database') as db_conn:
    print(f"Connected: {db_conn}")
    # Simulate database operation
    # Uncomment to simulate an exception
    # raise Exception("Something went wrong!")

"""
#### Explanation:
1. **`__enter__` method**:
   - Initializes and returns the resource (`self.connection` in this case) when entering the `with` block.

2. **`__exit__` method**:
   - Cleans up and releases the resource (`self.connection`) when exiting the `with` block.
   - It also handles any exceptions (`exc_type`, `exc_val`, `exc_tb`) that occur within the `with` block.

3. **Using `DatabaseConnection` context manager**:
   - Inside the `with` block, `DatabaseConnection('my_database') as db_conn` establishes a connection to `'my_database'`.
   - Operations on `db_conn` can be performed within the `with` block, and the connection is automatically closed (`__exit__` is called) when the block exits, ensuring proper cleanup.

Context managers provide a convenient and safe way to manage resources in Python, ensuring that resources are properly initialized and cleaned up, even in the presence of exceptions. They are particularly useful for handling file operations, database connections, locks, and other resources that need explicit setup and teardown.
"""