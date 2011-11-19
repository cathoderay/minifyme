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


if __name__ == "__main__":
    unittest.main()
