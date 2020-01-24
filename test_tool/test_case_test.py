from was_run import WasRun
from test_case import TestCase
from test_result import TestResult

class TestCaseTest(TestCase):

    def setUp(self):
        self.test= WasRun("testMethod")

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run(TestResult())
        assert("setUp testMethod tearDown " == test.log)
        print('testTemplateMethod done')

TestCaseTest("testTemplateMethod").run(TestResult())
