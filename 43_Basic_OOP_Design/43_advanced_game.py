class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

class Banana(Fruit):
    def __init__(self, color, flavor, poisonous, species):
        Fruit.__init__(self, "Banana", color, flavor, poisonous)
        self.species = species

    def detail_description(self):
        print "I am a special type of Banana: %s" % (self.species)

banana_type_01 = Banana(name="Banana", color="yellow", flavor="sweet", poisonous=False, species="Cuban")

banana_type_01.description()
banana_type_01.is_edible()
banana_type_01.detail_description()
