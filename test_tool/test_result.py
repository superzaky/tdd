class TestResult:
    # the constructor is called "__init__"for convenience
    def __init__(self):
        self.runCount = 0
    
    def testStarted(self):
        self.runCount = self.runCount + 1
