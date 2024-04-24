from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        raise NotImplementedError("Subclasses must implement my_abstract_method")

# Now you can subclass MyAbstractClass and implement the abstract method
class MyClass(MyAbstractClass):
    def my_abstract_method(self):
        print("Implementation of my_abstract_method")

# Create an instance of MyClass
obj = MyClass()

# Call the abstract method
obj.my_abstract_method()
