import unittest
import mlb_search
import mlb_predict
import csv

class TestCaseRun(unittest.TestCase):

    def test_nonmlb(self,keyword,teamarray):
        if keyword in teamarray:
            return "pass"
        else:
            return "fail"

    def test_mlb(self,keyword,teamarray):
        if keyword in teamarray:
            return "pass"
        else:
            return "fail"

    def test_gibtweet(self,line):
        if line == []:
            return "pass"
        else:
            return "fail"

    def test_istweet(self,filepath):
        if istype(filepath,csv):
            return "pass"
        else:
            return "fail"

    def test_isblank(self,line):
        if line==[]:
            return "pass"
        else:
            return "fail"

    def test_gettweets(self,keyword,output):
        if keyword in output:
            return "pass"
        else:
            return "fail"

if __name__=='__main__':
    unittest.main()
