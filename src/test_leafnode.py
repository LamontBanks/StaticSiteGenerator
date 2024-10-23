import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        leaf_node = LeafNode("This is some text!", tag="a", props={ "href": "http://www.example.com" })
        self.assertEqual(leaf_node.to_html(), "<a href=\"http://www.example.com\">This is some text!</a>")

    def test_to_html_multiple_props(self):
        leaf_node = LeafNode("This is some text!", tag="a", props={ "href": "http://www.example.com", "target": "_blank" })
        self.assertEqual(leaf_node.to_html(), "<a href=\"http://www.example.com\" target=\"_blank\">This is some text!</a>")

    def test_to_html_no_props(self):
        leaf_node = LeafNode("This is some text!", tag="a")
        self.assertEqual(leaf_node.to_html(), "<a>This is some text!</a>")

    def test_to_html_no_tag(self):
        leaf_node = LeafNode("This is some text!")
        self.assertEqual(leaf_node.to_html(), "This is some text!")
        
    def test_to_html_no_value(self):
        leaf_node = LeafNode("")
        leaf_node.value = None
        
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    def test_to_html_no_value(self):
        leaf_node = LeafNode("")
        leaf_node.value = None
        
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    def test_to_html_value_is_empty_string(self):
        leaf_node = LeafNode("", tag="a")
        self.assertEqual(leaf_node.to_html(), "<a></a>")

    def test_to_html_no_tag_and_value_is_empty_string(self):
        leaf_node = LeafNode("")
        self.assertEqual(leaf_node.to_html(), "")

if __name__ == "__main__":
    unittest.main()