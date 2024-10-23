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
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is some text", text_type=TextType.TEXT)), 
            HTMLNode(value="This is some text"))

    def test_empty_text(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="", text_type=TextType.TEXT)), 
            HTMLNode(value=""))
    
    def test_bold(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is some text", text_type=TextType.BOLD)), 
            HTMLNode(tag="b", value="This is some text"))

    def test_italic(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is some text", text_type=TextType.ITALIC)), 
            HTMLNode(tag="i", value="This is some text"))

    def test_code(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is some text", text_type=TextType.CODE)), 
            HTMLNode(tag="code", value="This is some text"))

    def test_link(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is a link", url="http://www.example.com", text_type=TextType.LINK)), 
            HTMLNode(tag="a", value="This is a link", props = { "href": "http://www.example.com" }))
        
    def test_link_no_href(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is a link", text_type=TextType.LINK)), 
            HTMLNode(tag="a", value="This is a link", props = { "href": "" }))

    def test_link_no_text(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="", url="http://www.example.com", text_type=TextType.LINK)), 
            HTMLNode(tag="a", value="", props = { "href": "http://www.example.com" }))

    def test_image(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is alt image text", url="http://www.example.com/image.png", text_type=TextType.IMAGE)), 
            HTMLNode(tag="img", value="", props = { "src": "http://www.example.com/image.png", "alt": "This is alt image text" }))
        
    def test_image_no_src(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="This is alt image text", text_type=TextType.IMAGE)), 
            HTMLNode(tag="img", value="", props = { "src": "", "alt": "This is alt image text" }))

    def test_image_no_alt(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text="", url="http://www.example.com/image.png", text_type=TextType.IMAGE)), 
            HTMLNode(tag="img", value="", props = { "src": "http://www.example.com/image.png", "alt": "" }))
            
        

if __name__ == "__main__":
    unittest.main()