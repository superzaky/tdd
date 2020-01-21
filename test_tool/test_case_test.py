from was_run import WasRun
from test_case import TestCase

class TestCaseTest(TestCase):

    def setUp(self):
        self.test= WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
        print('testRunning done')

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)
        print('testSetUp done')

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
