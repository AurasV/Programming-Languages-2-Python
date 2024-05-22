class Cube:
    def __init__(self, length):
        self.length = length

    def one_surface(self):
        return self.length * self.length

    def all_surface(self):
        return 6 * self.length * self.length

    def volume(self):
        return self.length * self.length * self.length


c = Cube(2)
print("One Surface Area: " + str(c.one_surface()))
print("All Surface Area: " + str(c.all_surface()))
print("Volume: " + str(c.volume()))
