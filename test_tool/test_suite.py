'''
Created on May 4, 2020

@author: Zaky
'''
from test_result import TestResult

class TestSuite:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.tests = []
        
    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        result = TestResult()
        for test in self.tests:
            test.run(result)
