class Enemy(object):
    def __init__(self, name, x):
        self.energy = x
        self.name = name

    def get_energy(self):
        print "Name: %s  Level: %s" % (self.name, self.energy)

enm1 = Enemy("Matt", 5)
enm2 = Enemy("Maya", 10)

enm1.get_energy()
enm2.get_energy()