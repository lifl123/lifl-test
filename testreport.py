import unittest
import HTMLTestRunner

class MyFirstUnit(unittest.TestCase):
    def test_casel(self):
        self.assertEqual("a","a","there are not equal")  #assert 断言
        print("11111111111111")

    def test_case_num(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("nnnnnn")

    def test_case_list(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3], "there are not equal")
        print("LLLLLLLLLLL")


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(MyFirstUnit("test_casel"))
    testunit.addTest(MyFirstUnit("test_case_num"))
    testunit.addTest(MyFirstUnit("test_case_list"))
    filename = 'E:\\Python\\TestFan-20181202\\report\\MyFirstUnitResult.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='MyFirstUnit测试报告',
    description='用例执行情况：')
    runner.run(testunit)        #run(套件名字)