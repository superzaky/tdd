class TestCase:
    pass

    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    # the run() method only uses attributes (i.e. self.name) from the superclass, so it probably belongs in the superclass
    def run(self):
        self.setUp()
        # the dynamic invocation of methods is called Pluggable Selector,
        exec("self." + self.name + "()")
