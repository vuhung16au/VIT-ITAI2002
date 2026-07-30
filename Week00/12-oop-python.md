# Introduction to Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods). Python is a multi-paradigm language that fully supports OOP.

## Key Concepts

1.  **Class**: A blueprint for creating objects. It defines the initial state (attributes) and behavior (methods) of the objects.
2.  **Object**: An instance of a class. It has its own unique data but shares the structure and behavior defined by the class.

## Example

Here is a simple example of defining a class and creating objects in Python:

```python
class Robot:
    # Class attribute (shared by all instances)
    environment = "Maze"

    # Constructor method to initialize an instance
    def __init__(self, name, battery_level):
        self.name = name                   # Instance attribute
        self.battery_level = battery_level # Instance attribute

    # Instance method
    def clean(self):
        return f"{self.name} the vacuum cleaner is cleaning the {self.environment}!"

# Creating objects (instances of the Robot class)
roomba = Robot("Roomba", 100)
deebot = Robot("Deebot", 85)

# Accessing attributes
print(roomba.name)          # Output: Roomba
print(deebot.environment)   # Output: Maze

# Calling methods
print(roomba.clean())       # Output: Roomba the vacuum cleaner is cleaning the Maze!
```

## Basic Principles of OOP

*   **Encapsulation**: Grouping related data and methods together within a class. In Python, this is mostly done by convention (e.g., prefixing attributes with an underscore `_` to indicate they are intended for internal use).
*   **Inheritance**: Creating a new class (child class) that inherits attributes and methods from an existing class (parent class), promoting code reuse.
*   **Polymorphism**: The ability to use a unified interface to operate on multiple types of objects (e.g., different classes having a method with the same name).
