from was_run import WasRun
from test_case import TestCase

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
        print('done')
TestCaseTest("testRunning").run()
