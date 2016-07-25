class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

dad = Parent()
son = Child("test")

dad.altered()
son.altered()