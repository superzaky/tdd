from was_run import WasRun
from test_case import TestCase
from test_result import TestResult

class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(TestResult())
        assert("setUp testMethod tearDown " == test.log)
        print('testTemplateMethod done')
        
    def testResult(self):
        test = WasRun("testMethod")
        result= test.run(TestResult())
        assert("1 run, 0 failed" == result.summary())
        print('testResult done')
        
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run(TestResult())
        assert("1 run, 1 failed", result.summary())
        print('testFailedResult done')

TestCaseTest("testTemplateMethod").run(TestResult())
TestCaseTest("testResult").run(TestResult())
TestCaseTest("testFailedResult").run(TestResult())
