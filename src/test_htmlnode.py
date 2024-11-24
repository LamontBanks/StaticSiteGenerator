import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        # Single prop
        html_node = HTMLNode(value="link to example.com", props={'url': 'http://www.example.com'})
        # Has leading space
        expected_props_html = ' url="http://www.example.com"' 
        self.assertEqual(html_node.props_to_html(), expected_props_html)

        # Multiple props
        html_node = HTMLNode(props={'alt': 'image alt text', 'src': 'http://www.example.com/image.png'})
        # Has leading space
        expected_props_html = ' alt="image alt text" src="http://www.example.com/image.png"'
        self.assertEqual(html_node.props_to_html(), expected_props_html)

        # No props
        html_node = HTMLNode()
        expected_props_html = ""
        self.assertEqual(html_node.props_to_html(), expected_props_html)


    def test_to_html_raises_error(self):
        html_node = HTMLNode()

        with self.assertRaises(NotImplementedError):
            html_node.to_html()

if __name__ == "__main__":
    unittest.main()