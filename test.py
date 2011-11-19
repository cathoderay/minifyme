import unittest

import minifyme


class Minifyme(unittest.TestCase):
    def testRemovingLineFeeds(self):
        input = """
function a() {
    var x = 1;
}
"""        
        output = minifyme.minifyme(input)
        self.assertTrue(output.count('\n') == 0)

    def testRemovingSlashSlashComments(self):
        input = """
//my wonderful comment
function a() {
    //i'm inside my wonderful function
    var x = 1;
}"""
        output = minifyme.minifyme(input)
        self.assertTrue(output.count('/') == 0)

    def testCantRemoveSlashSlashInsideStrings(self):
        input = """
function a() {
    //a comment
    var x = "//foo" //bar;
}"""
        output = minifyme.minifyme(input)
        self.assertTrue(output.count('/') == 2)
        self.assertTrue(output.find("//bar") < 0)
        self.assertTrue(output.find("//foo") > 0)


if __name__ == "__main__":
    unittest.main()
