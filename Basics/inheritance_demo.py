class ParentClass():
    def __init__(self):
        print("Parent class instance")

    def parent_method(self):
        print("Parents Money")

class ChildClass(ParentClass):
    pass

p = ParentClass()
p.parent_method()