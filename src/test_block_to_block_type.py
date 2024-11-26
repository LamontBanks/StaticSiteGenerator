import unittest
from markdown_blocks import *

class TestBlockToBlockType(unittest.TestCase):

    def test_heading_blocks(self):
        # H1 - H6
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "## Heading 2"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "### Heading 3"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "#### Heading 4"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "##### Heading 5"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # "H7+" is normal text
        block = "######## Heading 7"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)
        block = "######## Heading 8"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

    def test_code_blocks(self):
        block = "```some\nsample\n    code()```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_blocks(self):
        block = "> some\n> fancy\n> quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        # Wrong format => Normal text
        block = "> some\n fancy\n quote"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

    def test_unordered_list_blocks(self):
        # Only dashes
        block = "- Milk\n- Bread\n- Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        # Only asterisks
        block = "* Milk\n* 1 Bread\n* Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        # Mix dashes
        block = "* Milk\n- 1 Bread\n* Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        # Wrong format => Normal text
        block = "+ Milk\n+ Bread\n+ Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

    def test_ordered_list_blocks(self):
        block = "1. Milk\n2. Bread\n3. Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        # Out of order => normal text
        block = "2. Milk\n1. Bread\n3. Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

        # Doesn't start at 1 => normal text
        block = "3. Milk\n4. Bread\n5. Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

        # Missing numbers => normal text
        block = "1. Milk\n Bread\n3. Eggs"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

    def test_normal_blocks(self):
        block = "This is plain text"
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

        # Empty text => normal
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.NORMAL)

if __name__ == "__main__":
    unittest.main()