import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This a text node", TextType.TEXT)
        node2 = TextNode("This a text node", TextType.TEXT)

        self.assertEqual(node, node2)

    def test_diff_text_not_eq(self):
        node = TextNode("This a text node", TextType.TEXT)
        node2 = TextNode("This is not a text node", TextType.TEXT)

        self.assertNotEqual(node, node2)

    def test_diff_text_type_not_eq(self):
        node = TextNode("This a text node", TextType.TEXT)
        node2 = TextNode("This a text node", TextType.HTML)

        self.assertNotEqual(node, node2)

    def test_diff_url_not_eq(self):
        node = TextNode("This a text node", TextType.TEXT, "www.abc.com")
        node2 = TextNode("This a text node", TextType.TEXT, "www.xyz.com")

        self.assertNotEqual(node, node2)

    def test_repr(self):
        text = "This a text node"
        text_type = TextType.TEXT
        url = "http://www.example.com"

        node = TextNode(text, TextType.TEXT, url)
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type}, {url})")

    def test_repr_no_url(self):
        text = "This a text node"
        text_type = TextType.TEXT

        node = TextNode(text, TextType.TEXT)
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type}, None)")
    
    def test_repr_empty_values(self):
        text = ""
        text_type = ""

        node = TextNode(text, "")
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type}, None)")

### 

if __name__ == "__main__":
    unittest.main()