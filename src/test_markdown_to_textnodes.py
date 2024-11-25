import unittest

from markdown_to_textnodes import *
from textnode import *

class testMarkdownToTextNodes(unittest.TestCase):

    def test_markdown_mix_to_textnode(self):
        markdown = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        expected_text_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]

        self.assertEqual(text_to_textnodes(markdown), expected_text_nodes)

    def test_single_markdown_textnode(self):
        # Bold
        markdown = 'This is **text**'
        expected_text_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD)
        ]
        self.assertEqual(text_to_textnodes(markdown), expected_text_nodes)

        # Italic
        markdown = ' with an *italic* word and a '
        expected_text_nodes = [
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(markdown), expected_text_nodes)

        # Code
        markdown = '`code block` and an '
        expected_text_nodes = [
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(markdown), expected_text_nodes)

        # Image
        markdown = ' and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)'
        expected_text_nodes = [
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(text_to_textnodes(markdown), expected_text_nodes)

        # Link
        markdown = ' and a [link](https://boot.dev)'
        expected_text_nodes = [
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        self.assertEqual(text_to_textnodes(markdown), expected_text_nodes)

        # Plain text
        markdown = 'This is plain text.'
        expected_text_nodes = [
            TextNode("This is plain text.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(markdown), expected_text_nodes)