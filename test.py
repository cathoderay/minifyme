import unittest

import minifyme


class Minifyme(unittest.TestCase):
    #line feeds tests
    def testRemovingLineFeeds(self):
        input = r"""
function a() {
    var x = 1;
    var y = "\n"
}
"""        
        output = minifyme.remove_line_feeds(input)
        self.assertEqual(0, output.count('\n'))


    #line comments tests
    def testRemovingSlashSlashComments(self):
        input = r"""
//my wonderful comment
function a() {
    //i'm inside my wonderful function
    var x = 1;
}"""
        output = minifyme.remove_line_comments(input)
        self.assertEqual(0, output.count('/'))


    def testCantRemoveSlashSlashInsideStrings(self):
        input = r'var x = "//foo" //bar;'
        output = minifyme.remove_line_comments(input)
        self.assertEqual(2, output.count(r'/'))
        self.assertTrue(output.find(r"//bar") < 0)
        self.assertTrue(output.find(r"//foo") > 0)


    def testCantRemoveSlashSlashInsideRegex(self):
        input = r'var x = /^\/\//;'
        output = minifyme.remove_line_comments(input)
        self.assertEqual(4, output.count(r'/'))
        self.assertTrue(output.find(r'/^\/\//;') > 0)


    def testScapesAreInterpretedInsideStrings(self):
        input = r'var a = "bla\"test//!";'
        output = minifyme.remove_line_comments(input)
        self.assertTrue(output.find(r"a\"test//") > 0)


    def testCantRemoveMultilinecommentWhenRemovingLineComments(self):
        input = r'/* test*/'
        output = minifyme.remove_line_comments(input)
        self.assertTrue(output.find(r'/* test*/') >= 0)


    #remove multiline comments
    def testRemovingMultilineComments(self):
        input = r"""
/*
    A mind once  
    stretched by a new idea
    never returns to its
    original dimension
*/
    var a = 1;
"""
        output = minifyme.remove_multiline_comments(input)    
        self.assertTrue(output.find(r'mind') < 0)
        self.assertTrue(output.find(r'dimension') < 0)
        self.assertTrue(output.find(r'/*') < 0)
        self.assertTrue(output.find(r'*/') < 0)
        self.assertTrue(output.find(r'var') > 0)


    def testCantRemoveFakeMultilineCommentsInsideStrings(self):
        input = r'var a = "/*asdf*/";'
        output = minifyme.remove_multiline_comments(input)
        self.assertTrue(output.find(r'"/*asdf*/"') > 0)

    
    def testCantRemoveFakeMultilineCommentsInsideRegex(self):
        input = r'var a = /\/*asdf*\//;'
        output = minifyme.remove_multiline_comments(input)
        self.assertTrue(output.find(r'/*asdf*\/') > 0)


    def testCantRemoveLineCommentWhenRemovingMultilineComments(self):
        input = r'// /*asdf' 
        output = minifyme.remove_multiline_comments(input)
        self.assertTrue(output.find(r'// /*asdf') >= 0)


    #remove leading and trailing whitespaces
    def testRemovingLeadingAndTrailingWhitespaces(self):
        input = """
    function() {  
\t\r        var x = 1;   
"""        
        output = minifyme.remove_leading_and_trailing_whitespaces(input)
        self.assertEqual(4, output.count(r' '))
        self.assertEqual(0, output.count(r'\t'))
        self.assertEqual(0, output.count(r'\r'))


if __name__ == "__main__":
    unittest.main()
