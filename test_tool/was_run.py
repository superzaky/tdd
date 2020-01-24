from test_case import TestCase

class WasRun(TestCase):
    # the constructor is called "__init__"for convenience
    def __init__(self, name):
        self.wasRun= None
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "
    
    def testMethod(self):
        self.log= self.log + "testMethod "
        
    def tearDown(self):
        self.log = self.log + "tearDown "
