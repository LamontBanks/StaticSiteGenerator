import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from node_converter import text_node_to_html_node

class TestNodeConverter(unittest.TestCase):

    '''
    TextType.TEXT: This should become a LeafNode with no tag, just a raw text value.
        Empty string
TextType.BOLD: This should become a LeafNode with a "b" tag and the text
TextType.ITALIC: "i" tag, text
TextType.CODE: "code" tag, text
TextType.LINK: "a" tag, anchor text, and "href" prop
    empty href
    no text
TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    no src
    no alt
    '''
    def test_text_node(self):
        text_node = TextNode(text="This is some text", text_type=TextType.TEXT)

        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is some text", text_type=TextType.TEXT)), 
            HTMLNode(value="This is some text"))
        

if __name__ == "__main__":
    unittest.main()