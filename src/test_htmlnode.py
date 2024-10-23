import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single_property(self):
        html_node = HTMLNode(tag='a',
                               value='abc',
                               props={ "a": "xyz"})
        
        # Leading space is intentional
        expected_html = " " + "a=\"xyz\""
        
        self.assertEqual(html_node.props_to_html(), expected_html)

    def test_props_to_html_multiple_properties(self):
        html_node = HTMLNode(tag='a',
                               value='abc',
                               props={'property1': 'value1', 'property2': 123, 'property3': 'value3'})
        
        
        # All properties must be quoted, even ints
        expected_html = " " + "property1=\"value1\" property2=\"123\" property3=\"value3\""

        self.assertEqual(html_node.props_to_html(), expected_html)

    def test_props_to_html_empty(self):
        html_node = HTMLNode(tag='a',
                               value='abc')
        
        expected_html = ""
        
        self.assertEqual(html_node.props_to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()