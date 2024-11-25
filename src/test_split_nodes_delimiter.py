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

    def test_extract_markdown_images(self):
        # Image markdown
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_tuples = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'),
                                 ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(extract_markdown_images(text), expected_tuples)

        # No matches
        text = "This is text without any image markdown"
        expected_tuples = []
        self.assertEqual(extract_markdown_images(text), expected_tuples)

        # Mix Markdown, only 1 match found
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_tuples = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(extract_markdown_images(text), expected_tuples)

    def test_extract_markdown_links(self):
        # link markdown
        text = "This is text with a [link text 1](https://www.example.com) and [link text 2](https://www.example.2.com)"
        expected_tuples = [('link text 1', 'https://www.example.com'),
                            ('link text 2', 'https://www.example.2.com')]
        self.assertEqual(extract_markdown_links(text), expected_tuples)

        # No matches
        text = "This is text without any link markdown"
        expected_tuples = []
        self.assertEqual(extract_markdown_links(text), expected_tuples)

        # Mix Markdown, only 1 match found
        text = "This is text with a ![image alt text](https://www.example.com/image.png) and [link text 2](https://www.example.2.com)"
        expected_tuples = [('link text 2', 'https://www.example.2.com')]
        self.assertEqual(extract_markdown_links(text), expected_tuples)

if __name__ == "__main__":
    unittest.main()