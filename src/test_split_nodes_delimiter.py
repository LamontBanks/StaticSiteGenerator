import unittest

from split_nodes_delimiter import *
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_code(self):
        node = TextNode("This is text with a `code block` word and here's `another` and `another one`.", TextType.TEXT)

        expected_split_nodes = [
            TextNode(text="This is text with a ", text_type=TextType.TEXT, url=None),
            TextNode(text="code block", text_type=TextType.CODE, url=None),
            TextNode(text=" word and here's ", text_type=TextType.TEXT, url=None),
            TextNode(text="another", text_type=TextType.CODE, url=None),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="another one", text_type=TextType.CODE, url=None),
            TextNode(text=".", text_type=TextType.TEXT, url=None)
        ]

        self.assertEqual(split_nodes_delimiter([node], TextDelimiter.CODE.value, TextType.CODE), expected_split_nodes)

    def test_split_italic(self):
        node = TextNode("This is text with an *italic* word and here's *another* and *another one*.", TextType.TEXT)

        expected_split_nodes = [
            TextNode(text="This is text with an ", text_type=TextType.TEXT, url=None),
            TextNode(text="italic", text_type=TextType.ITALIC, url=None),
            TextNode(text=" word and here's ", text_type=TextType.TEXT, url=None),
            TextNode(text="another", text_type=TextType.ITALIC, url=None),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="another one", text_type=TextType.ITALIC, url=None),
            TextNode(text=".", text_type=TextType.TEXT, url=None)
        ]

        self.assertEqual(split_nodes_delimiter([node], TextDelimiter.ITALIC.value, TextType.ITALIC), expected_split_nodes)

    def test_split_bold(self):
        node = TextNode("This is text with a **bold** word and here's **another** and **another one**.", TextType.TEXT)

        expected_split_nodes = [
            TextNode(text="This is text with a ", text_type=TextType.TEXT, url=None),
            TextNode(text="bold", text_type=TextType.BOLD, url=None),
            TextNode(text=" word and here's ", text_type=TextType.TEXT, url=None),
            TextNode(text="another", text_type=TextType.BOLD, url=None),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="another one", text_type=TextType.BOLD, url=None),
            TextNode(text=".", text_type=TextType.TEXT, url=None)
        ]

        self.assertEqual(split_nodes_delimiter([node], TextDelimiter.BOLD.value, TextType.BOLD), expected_split_nodes)

if __name__ == "__main__":
    unittest.main()