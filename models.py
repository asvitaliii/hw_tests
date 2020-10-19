class Child:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        self.__age = age


class Parent:
    def __init__(self, name: str, age: int, children: list):
        self.__name = name
        self.__age = age
        self.__children = children

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_children(self):
        return self.__children

    def set_age(self, age: int):
        self.__age = age

    def add_children(self, children: Child):
        if children not in self.__children:
            self.__children.append(children)

    def detdom(self, children: Child):
        if children in self.__children:
            self.__children.remove(children)
