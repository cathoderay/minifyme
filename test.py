import unittest

import minifyme


class Minifyme(unittest.TestCase):
    #line feeds tests
    def test_removing_line_feeds(self):
        input = r'''
        function a() {
            var x = 1;
            var y = "\n"
        }
        '''
        output = minifyme.remove_line_feeds(input)
        self.assertEqual(0, output.count('\n'))

    #line comments tests
    def test_removing_line_comments(self):
        input = r'''
        //first comment
        function a() {
            //second comment
            var x = 1;
        }'''
        output = minifyme.remove_line_comments(input)
        self.assertEqual(0, output.count('/'))
        self.assertTrue(output.find('first comment') < 0)
        self.assertTrue(output.find('second comment') < 0)

    def test_cant_remove_double_slash_inside_strings(self):
        input = r'var x = "//foo" //bar;'
        output = minifyme.remove_line_comments(input)
        self.assertEqual(2, output.count(r'/'))
        self.assertTrue(output.find(r"//bar") < 0)
        self.assertTrue(output.find(r"//foo") > 0)

    def test_cant_remove_double_slash_inside_regex(self):
        input = r'var x = /^\/\//;'
        output = minifyme.remove_line_comments(input)
        self.assertEqual(4, output.count(r'/'))
        self.assertTrue(output.find(r'/^\/\//;') > 0)

    def test_scapes_are_interpreted_inside_strings(self):
        input = r'var a = "bla\"test//!";'
        output = minifyme.remove_line_comments(input)
        self.assertTrue(output.find(r"a\"test//") > 0)

    def test_cant_remove_multiline_comment_when_removing_line_comments(self):
        input = r'/* test*/'
        output = minifyme.remove_line_comments(input)
        self.assertTrue(output.find(r'/* test*/') >= 0)

    #remove multiline comments
    def test_removing_multiline_comments(self):
        input = r'''
        /*
          A mind once
          stretched by a new idea
          never returns to its
          original dimension
        */
        var a = 1;
        '''
        output = minifyme.remove_multiline_comments(input)    
        self.assertTrue(output.find(r'mind') < 0)
        self.assertTrue(output.find(r'dimension') < 0)
        self.assertTrue(output.find(r'/*') < 0)
        self.assertTrue(output.find(r'*/') < 0)
        self.assertTrue(output.find(r'var') > 0)

    def test_cant_remove_fake_multiline_comments_inside_strings(self):
        input = r'var a = "/*asdf*/";'
        output = minifyme.remove_multiline_comments(input)
        self.assertTrue(output.find(r'"/*asdf*/"') > 0)
    
    def test_cant_remove_fake_multiline_comments_inside_regex(self):
        input = r'var a = /\/*asdf*\//;'
        output = minifyme.remove_multiline_comments(input)
        self.assertTrue(output.find(r'/*asdf*\/') > 0)

    def test_cant_remove_line_comment_when_removing_multiline_comments(self):
        input = r'// /*asdf' 
        output = minifyme.remove_multiline_comments(input)
        self.assertTrue(output.find(r'// /*asdf') >= 0)

    #remove leading and trailing whitespaces
    def test_removing_leading_and_trailing_whitespaces(self):
        input = r'''
        function() {  
	        var x = 1;   
        '''
        output = minifyme.remove_leading_and_trailing_whitespaces(input)
        self.assertEqual(4, output.count(r' '))
        self.assertEqual(0, output.count(r'\t'))
        #test '\r'

    def test_backslash_end_of_regex(self):
        input = "var x = /\\/g; //foo bar"
        output = minifyme.remove_line_comments(input)
        self.assertTrue(output.find("//foo bar") < 0)


if __name__ == "__main__":
    unittest.main()
