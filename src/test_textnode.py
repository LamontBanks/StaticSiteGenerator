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

    def test_same_text_diff_text_type_not_eq(self):
        node = TextNode("abc", TextType.TEXT)
        node2 = TextNode("abc", TextType.LINK)

        self.assertNotEqual(node, node2)

    def test_diff_url_not_eq(self):
        node = TextNode("This a link", TextType.LINK, "www.abc.com")
        node2 = TextNode("This a link", TextType.LINK, "www.xyz.com")

        self.assertNotEqual(node, node2)

    def test_repr(self):
        text = "This is a link"
        text_type = TextType.LINK
        url = "http://www.example.com"

        node = TextNode(text, TextType.LINK, url)
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type}, {url})")

    def test_repr_no_url_set(self):
        text = "This a text node"
        text_type = TextType.TEXT

        node = TextNode(text, TextType.TEXT)
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type}, None)")
    
    def test_repr_empty_strings(self):
        text = ""
        text_type = ""

        node = TextNode(text, "")
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type}, None)")

### 

if __name__ == "__main__":
    unittest.main()