from was_run import WasRun
from test_case import TestCase

class TestCaseTest(TestCase):

    def setUp(self):
        self.test= WasRun("testMethod")

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
        print('testTemplateMethod done')

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
