import unittest

import minifyme


class Minifyme(unittest.TestCase):
    def testRemovingLineFeeds(self):
        input = """
function() {
    var x = 1;
}
"""        
        output = minifyme.minifyme(input)
        self.assertTrue(output.count('\n') == 0)

    def testremoveSlashSlashComments(self):
        input = """
//my wonderful comment
function() {
    //i'm inside my wonderful function
    var x = 1;
}"""
        output = minifyme.minifyme(input)
        self.assertTrue(output.count('/') == 0)
        self.assertTrue(output.count('\n') == 0)

    #TODO: test // in strings

if __name__ == "__main__":
    unittest.main()
