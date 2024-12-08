import inspect


def introspection_info(obj):
    """
    Perform detailed introspection of the given object.

    Args:
        obj: Any Python object to introspect.

    Returns:
        dict: A dictionary with details about the object's type, attributes, methods, module, etc.
    """
    # Dictionary to store introspection details
    obj_info = {}

    # Get the type of the object
    obj_info["type"] = type(obj).__name__

    # Separate attributes and methods
    obj_info["attributes"] = [item for item in dir(obj) if not callable(getattr(obj, item))]
    obj_info["methods"] = [item for item in dir(obj) if callable(getattr(obj, item))]

    # Get module information
    obj_info["module"] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

    # Get the docstring
    obj_info["docstring"] = inspect.getdoc(obj)

    return obj_info


# Testing the function
if __name__ == "__main__":
    # Test with a built-in object
    number_info = introspection_info(42)
    print("Introspection of an integer object:")
    print(number_info)

    # Test with a string
    string_info = introspection_info("Hello")
    print("\nIntrospection of a string object:")
    print(string_info)


    # Define a custom class for testing
    class Person:
        """A simple class to represent a person."""

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hello, my name is {self.name}."


    # Create an instance of the custom class
    person = Person("Alice", 30)
    person_info = introspection_info(person)
    print("\nIntrospection of a custom Person object:")
    print(person_info)
