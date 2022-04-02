# Abstract classes

'''In an online shopping app, we only have specific types of products. We don’t have something
called a Product itself. In that sense, an object of Product class would not represent a real world object,
because a Product is just an abstract concept. While shopping, we purchase
types of products, not a product itself. Thus the best practice is not to create object of the parent class.'''

from abc import ABCMeta
class Product(metaclass=ABCMeta):
    def return_policy(self):
        pass

'''If an abstract class should never be instantiated, then what is the use of such a class? 
The only way we can use an abstract class is to make other classes inherit from the abstract class. 
An abstract class is meant to be sub classed.'''



class Furniture(Product):
    pass

Furniture()