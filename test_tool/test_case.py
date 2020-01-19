class TestCase:
    pass

    def __init__(self, name):
        self.name= name

    # the run() method only uses attributes from the superclass, so it probably belongs in the superclass
    def run(self):
        # the dynamic invocation of methods is called Pluggable Selector,
        exec("self." + self.name + "()")
