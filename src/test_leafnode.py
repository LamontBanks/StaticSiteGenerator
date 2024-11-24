import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        # Full HTML tag
        leaf_node = LeafNode(tag="myTag",
                             value="some value",
                             props={'alt': 'some alt text', 'src': 'http://www.example.com/image.png'})
        expected_html = '<myTag alt="some alt text" src="http://www.example.com/image.png">some value</myTag>'
        self.assertEqual(leaf_node.to_html(), expected_html)

        # No tag = return plaintext value
        leaf_node =  LeafNode(tag=None, value="some value")
        expected_html = "some value"
        self.assertEqual(leaf_node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()