from take_time import timeit


#
# Exercise 10
#
class Rectangle(object):
    def __init__(self, s0, s1):
        self.s0 = s0
        self.s1 = s1

    @timeit
    def perimeter(self):
        return 2 * (self.s0 + self.s1)

    def area(self):
        return self.s0 * self.s1

square = Rectangle(5, 5)
print square.perimeter()
print square.area()


#
# Exercise 11
#
from math import pi


class Circle(object):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2

circle = Circle(1)
print circle.perimeter()
print circle.area()


#
# Exercise 12
#
class Person(object):
    def __init__(self, name, surname):
        self.name = name.capitalize()
        self.surname = surname.capitalize()


class Contact(Person):
    def __init__(self, address=None, mobile=None, phone=None, *args, **kargs):
        # super is a function that call the method of the parent object
        super(Contact, self).__init__(*args, **kargs)
        self.address = address
        self.mobile = mobile
        self.phone = phone


class NiceContact(Contact):
    def __init__(self, *args, **kargs):
        super(NiceContact, self).__init__(*args, **kargs)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)

    def __repr__(self):
        return "NiceContact(%r, %r)" % (self.name, self.surname)


#
# Exercise 12
#


class Contact(Person):
    def _get_phone(self):
        return self._phone

    def _set_phone(self, phone):
        if phone.isdigit():
            if len(phone)>8:
                self._phone = phone
            else:
                raise TypeError("Phone number must be longer than 8 characters")
        else:
            raise TypeError("Phone number must contain only numbers")

    phone = property(fget=_get_phone, fset=_set_phone)

    @property
    def complete_name(self):
        return "%s %s" % (self.name, self.surname)

    def __init__(self, address=None, mobile=None, phone=None, *args, **kargs):
        # super is a function that call the method of the parent object
        super(Contact, self).__init__(*args, **kargs)
        self.address = address
        self.mobile = mobile
        self.phone = phone