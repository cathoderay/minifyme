import unittest

import minifyme


class Minifyme(unittest.TestCase):
    def testRemovingLineFeeds(self):
        input = """
function a() {
    var x = 1;
}
"""        
        output = minifyme.remove_line_feeds(input)
        self.assertEqual(0, output.count('\n'))

    def testRemovingSlashSlashComments(self):
        input = """
//my wonderful comment
function a() {
    //i'm inside my wonderful function
    var x = 1;
}"""
        output = minifyme.remove_line_comments(input)
        self.assertEqual(0, output.count('/'))

    def testCantRemoveSlashSlashInsideStrings(self):
        input = """
function a() {
    //a comment
    var x = "//foo" //bar;
}"""
        output = minifyme.remove_line_comments(input)
        self.assertEqual(2, output.count('/'))
        self.assertTrue(output.find("//bar") < 0)
        self.assertTrue(output.find("//foo") > 0)

    def testCantRemoveSlashSlashInsideRegex(self):
        input = """
function a() {
    //a comment
    var x = /\sdf\//;
}"""
        output = minifyme.remove_line_comments(input)
        self.assertEqual(3, output.count('/'))
        self.assertTrue(output.find('x = /\sdf\//') > 0)

    def testRemovingMultilineComments(self):
        input = """
/*
    A mind once  
    stretched by a new idea
    never returns to its
    original dimension
*/
    var a = 1;
"""
        output = minifyme.remove_multiline_comments(input)    
        self.assertTrue(output.find("mind") < 0)
        self.assertTrue(output.find("dimension") < 0)
        self.assertTrue(output.find("var") > 0)


if __name__ == "__main__":
    unittest.main()
