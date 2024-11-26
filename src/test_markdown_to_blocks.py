import unittest

from markdown_to_blocks import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_multi_line_markdown(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        expected_blocks = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_no_empty_lines_markdown(self):
        markdown = """
# This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item


* This is another list item
"""
        expected_blocks = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item',
            '* This is another list item'
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_only_newlines_markdown(self):
        markdown = """






"""
        expected_blocks = []

        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

if __name__ == "__main__":
    unittest.main()