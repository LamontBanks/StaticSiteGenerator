import unittest

from htmlnode import *
from leafnode import *
from parentnode import *
from markdown_to_html_node import *

class TestMarkdownToHtmlNode(unittest.TestCase):

    def set_up(self):
        self.maxDiff = None

    def test_full_conversion(self):
        markdown = """
# Plaintext Formatting

This is **text** with an *italic* word and `inline code`.
Here's an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link to Boot.dev](https://boot.dev)

## Lists

Ordered List

1. First item
2. Second item
3. Third item

Unordered List

- Item one
- Item two
- Item three

### Headings

##### H5 Heading

###### H6 Code Block

```
class TestClass():
    def __init__(self, x, y=5):
        self.x = x
        self.y = y + x
    def sum(self):
        return self.x + self.y
```

#### Some Block Quotes

> As above, so below
> Once more, with feeling
> I'm not arrogant, I'm right!
"""
        expected_html_nodes = ParentNode(tag=HTMLTag.DIV, children=[
                LeafNode(tag=HTMLTag.HEADING_1, value="Plaintext Formatting"),

                ParentNode(tag=HTMLTag.PARAGRAPH, children=[
                    LeafNode(tag=HTMLTag.TEXT, value="This is "),
                    LeafNode(tag=HTMLTag.BOLD, value="text"),
                    LeafNode(tag=HTMLTag.TEXT, value=" with an "),
                    LeafNode(tag=HTMLTag.ITALIC, value="italic"),
                    LeafNode(tag=HTMLTag.TEXT, value=" word and "),
                    LeafNode(tag=HTMLTag.CODE, value="inline code"),
                    # Line break and period are together
                    LeafNode(tag=HTMLTag.TEXT, value=".\nHere's an "),
                    LeafNode(tag=HTMLTag.IMAGE, value="", props={ 'src': 'https://i.imgur.com/fJRm4Vk.jpeg', 'alt': 'obi wan image'}),
                    LeafNode(tag=HTMLTag.TEXT, value=" and a "),
                    LeafNode(tag=HTMLTag.LINK, value='link to Boot.dev', props={ 'href': 'https://boot.dev'})
                ]),
                    
                LeafNode(tag=HTMLTag.HEADING_2, value="Lists"),

                ParentNode(tag=HTMLTag.PARAGRAPH, children=[
                    LeafNode(tag=HTMLTag.TEXT, value="Ordered List")
                ]),

                ParentNode(tag=HTMLTag.ORDERED_LIST, children=[
                    ParentNode(tag=HTMLTag.LIST_ITEM, children=[
                        LeafNode(tag=HTMLTag.TEXT, value="First item")
                    ]),
                    ParentNode(tag=HTMLTag.LIST_ITEM, children=[
                        LeafNode(tag=HTMLTag.TEXT, value="Second item")
                    ]),
                    ParentNode(tag=HTMLTag.LIST_ITEM, children=[
                        LeafNode(tag=HTMLTag.TEXT, value="Third item")
                    ])
                ]),

                ParentNode(tag=HTMLTag.PARAGRAPH, children=[
                    LeafNode(tag=HTMLTag.TEXT, value="Unordered List")
                ]),

                ParentNode(tag=HTMLTag.UNORDERED_LIST, children=[
                    ParentNode(tag=HTMLTag.LIST_ITEM, children=[
                        LeafNode(tag=HTMLTag.TEXT, value="Item one")
                    ]),
                    ParentNode(tag=HTMLTag.LIST_ITEM, children=[
                        LeafNode(tag=HTMLTag.TEXT, value="Item two")
                    ]),
                    ParentNode(tag=HTMLTag.LIST_ITEM, children=[
                        LeafNode(tag=HTMLTag.TEXT, value="Item three")
                    ])
                ]),

                LeafNode(tag=HTMLTag.HEADING_3, value="Headings"),
                LeafNode(tag=HTMLTag.HEADING_5, value="H5 Heading"),
                LeafNode(tag=HTMLTag.HEADING_6, value="H6 Code Block"),

                ParentNode(tag=HTMLTag.PRE, children=[
                    LeafNode(tag=HTMLTag.CODE, value="class TestClass():\n    def __init__(self, x, y=5):\n        self.x = x\n        self.y = y + x\n    def sum(self):\n        return self.x + self.y")
                ]),

                LeafNode(tag=HTMLTag.HEADING_4, value="Some Block Quotes"),

                LeafNode(tag=HTMLTag.BLOCKQUOTE, value="As above, so below\nOnce more, with feeling\nI'm not arrogant, I'm right!")
            ])
    
        self.assertEqual(markdown_to_html_node(markdown), expected_html_nodes)

    def test_extract_title(self):
        markdown = """
# Plaintext Formatting

This is **text** with an *italic* word and `inline code`.
Here's an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link to Boot.dev](https://boot.dev)

## Lists

Ordered List

1. First item
2. Second item
3. Third item
"""
        self.assertEqual(extract_title(markdown), 'Plaintext Formatting')

        # No title
        with self.assertRaises(Exception):
            extract_title("### Title")

if __name__ == "__main__":
    unittest.main()