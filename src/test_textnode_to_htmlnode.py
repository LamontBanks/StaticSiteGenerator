import unittest

from textnode import *
from htmlnode import *
from node_converter import text_node_to_html_node

class TestTextNodeToHTMLNodeConverter(unittest.TestCase):

    def test_text_node(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.TEXT, text="This is some text")), 
            HTMLNode(tag=HTMLTag.TEXT, value="This is some text"))

    def test_empty_text(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.TEXT, text="")), 
            HTMLNode(tag=HTMLTag.TEXT, value=""))
    
    def test_bold(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.BOLD, text="This is some text")), 
            HTMLNode(tag=HTMLTag.BOLD, value="This is some text"))

    def test_italic(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.ITALIC, text="This is some text")), 
            HTMLNode(tag=HTMLTag.ITALIC, value="This is some text"))

    def test_code(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.CODE, text="This is some text")), 
            HTMLNode(tag=HTMLTag.CODE, value="This is some text"))

    def test_link(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.LINK, text="This is a link", url="http://www.example.com")), 
            HTMLNode(tag=HTMLTag.LINK, value="This is a link", props = { "href": "http://www.example.com" }))
        
    def test_link_no_href(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.LINK, text="This is a link")), 
            HTMLNode(tag=HTMLTag.LINK, value="This is a link", props = { "href": None }))

    def test_link_no_text(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.LINK, text="", url="http://www.example.com")), 
            HTMLNode(tag=HTMLTag.LINK, value="", props = { "href": "http://www.example.com" }))

    def test_image(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.IMAGE, text="This is alt image text", url="http://www.example.com/image.png")),
            HTMLNode(tag=HTMLTag.IMAGE, props = { "src": "http://www.example.com/image.png", "alt": "This is alt image text" }))
        
    def test_image_no_src(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.IMAGE, text="This is alt image text")), 
            HTMLNode(tag=HTMLTag.IMAGE, props = { "src": None, "alt": "This is alt image text" }))

    def test_image_empty_alt_text(self):
        self.assertEqual(text_node_to_html_node(
            TextNode(text_type=TextType.IMAGE, text="", url="http://www.example.com/image.png")), 
            HTMLNode(tag=HTMLTag.IMAGE, props = { "src": "http://www.example.com/image.png", "alt": "" }))
            

if __name__ == "__main__":
    unittest.main()