import unittest
from textnode import *

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        text_node_1 = TextNode("sample_function()", TextType.CODE)
        text_node_2 = TextNode("sample_function()", TextType.CODE)
        self.assertEqual(text_node_1, text_node_2)

        text_node_1 = TextNode("image alt text", TextType.IMAGE, 'http://example.com/image.png')
        text_node_2 = TextNode("different image alt text", TextType.IMAGE, 'http://example.com/image.png')
        self.assertNotEqual(text_node_1, text_node_2)

        text_node_1 = TextNode("image alt text", TextType.IMAGE)
        text_node_2 = TextNode("different image alt text", TextType.IMAGE, 'http://example.com/image.png')
        self.assertNotEqual(text_node_1, text_node_2)

        text_node_1 = TextNode("Sample Text", TextType.BOLD)
        text_node_2 = TextNode("Sample Text", TextType.ITALIC)
        self.assertNotEqual(text_node_1, text_node_2)

    def test_repr(self):
        text_node = TextNode("image alt text", TextType.IMAGE, 'http://example.com/image.png')
        expected_repr = "TextNode(text=image alt text, text_type=image, url=http://example.com/image.png)"
        self.assertEqual(text_node.__repr__(), expected_repr)

        text_node = TextNode("image alt text", TextType.IMAGE)
        expected_repr = "TextNode(text=image alt text, text_type=image, url=None)"
        self.assertEqual(text_node.__repr__(), expected_repr)

if __name__ == "__main__":
    unittest.main()