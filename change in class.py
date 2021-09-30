class Example:
    name = "Example"

    @classmethod
    def static(cls):
        print
        var = "%s static() called" % cls.name

class Offspring1(Example):
    name = "Offspring1"
    pass

class Offspring2(Example):
    name = "Offspring2"

    @classmethod
    def static(cls):
        print "%s static() called" % cls.name

Example.static()    # prints Example
Offspring1.static() # prints Offspring1
Offspring2.static() # prints Offspring2