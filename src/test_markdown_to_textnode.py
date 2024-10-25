import unittest
from markdown_to_textnode import split_nodes_delimiter
from textnode import TextNode, TextType, DelimiterType

class TestMarkdownToTextNode(unittest.TestCase):
    # Funtionality tested with DelimiterType.CODE
    # Other Delimiters have only the basic test
    def test_basic_conversion(self):
        nodes = [
            TextNode(text="This is text with a `code` word", text_type=TextType.TEXT)
        ]

        expected_nodes = [
            TextNode(text="This is text with a ", text_type=TextType.TEXT),
            TextNode(text="code", text_type=TextType.CODE),
            TextNode(text=" word", text_type=TextType.TEXT)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)

    def test_multiple_nodes(self):
        nodes = [
            TextNode(text="This is text with a `code` word", text_type=TextType.TEXT),
            TextNode(text="This is text without a code word", text_type=TextType.TEXT),
            TextNode(text="I guess we're doing plain `text` now?", text_type=TextType.TEXT),
            TextNode(text="Nope, full code. Welcome back.", text_type=TextType.CODE)
        ]

        expected_nodes = [
            TextNode(text="This is text with a ", text_type=TextType.TEXT),
            TextNode(text="code", text_type=TextType.CODE),
            TextNode(text=" word", text_type=TextType.TEXT),
            TextNode(text="This is text without a code word", text_type=TextType.TEXT),
            TextNode(text="I guess we're doing plain ", text_type=TextType.TEXT),
            TextNode(text="text", text_type=TextType.CODE),
            TextNode(text=" now?", text_type=TextType.TEXT),
            TextNode(text="Nope, full code. Welcome back.", text_type=TextType.CODE)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)
    
    def test_single_word(self):
        nodes = [
            TextNode(text="`print(\"hello world\")`", text_type=TextType.TEXT)
        ]

        expected_nodes = [
            TextNode(text="print(\"hello world\")", text_type=TextType.CODE)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)

    def test_multiple_words(self):
        nodes = [
            TextNode(text="Green functions: `.reduce()`, `.reuse()`, and `.recycle()`.", text_type=TextType.TEXT)
        ]

        expected_nodes = [
            TextNode(text="Green functions: ", text_type=TextType.TEXT),
            TextNode(text=".reduce()", text_type=TextType.CODE),
            TextNode(text=", ", text_type=TextType.TEXT),
            TextNode(text=".reuse()", text_type=TextType.CODE),
            TextNode(text=", and ", text_type=TextType.TEXT),
            TextNode(text=".recycle()", text_type=TextType.CODE),
            TextNode(text=".", text_type=TextType.TEXT),
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)


    def test_non_plaintext_words_not_modified(self):
        nodes = [
            TextNode(text="code", text_type=TextType.CODE),
            TextNode(text="bold text", text_type=TextType.BOLD),
            TextNode(text="italic text", text_type=TextType.ITALIC)
            # TODO: image and links
            # TextNode(text="code", text_type=TextType.IMAGE),
            # TextNode(text="code", text_type=TextType.LINK),
        ]

        expected_nodes = [
            TextNode(text="code", text_type=TextType.CODE),
            TextNode(text="bold text", text_type=TextType.BOLD),
            TextNode(text="italic text", text_type=TextType.ITALIC)
            # TODO: image and links would also be unaffected
            # TextNode(text="code", text_type=TextType.IMAGE),
            # TextNode(text="code", text_type=TextType.LINK)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)

    def test_mixed_words(self):
        # Delimited, empty strings will not generate nodes
        nodes = [
            TextNode(text="`code1`plain1`code2` plain2 `code3``code4  ` `` plain3 `` plain4 `` ``", text_type=TextType.TEXT)
        ]

        expected_nodes = [
            TextNode(text="code1", text_type=TextType.CODE),
            TextNode(text="plain1", text_type=TextType.TEXT),
            TextNode(text="code2", text_type=TextType.CODE),
            TextNode(text=" plain2 ", text_type=TextType.TEXT),
            TextNode(text="code3", text_type=TextType.CODE),
            TextNode(text="code4  ", text_type=TextType.CODE),
            TextNode(text=" ", text_type=TextType.TEXT),
            TextNode(text=" plain3 ", text_type=TextType.TEXT),
            TextNode(text=" plain4 ", text_type=TextType.TEXT),
            TextNode(text=" ", text_type=TextType.TEXT)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)

    # ""
    def test_empty_delimited_word(self):
        # Delimited, empty strings will not generate nodes
        nodes = [
            TextNode(text="``", text_type=TextType.TEXT)
        ]

        expected_nodes = [
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)

    def test_plaintext_empty_word(self):
        # Plain text, empty strings will not generate nodes
        nodes = [
            TextNode(text="", text_type=TextType.TEXT)
        ]

        expected_nodes = [
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)
         

    def test_only_delimiters(self):
        nodes = [
            TextNode(text="``````", text_type=TextType.TEXT)
        ]

        expected_nodes = [
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)

    def test_plain_text(self):
        nodes = [
            TextNode(text="plain text", text_type=TextType.TEXT)
        ]

        expected_nodes = [
            TextNode(text="plain text", text_type=TextType.TEXT)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.CODE.value, TextType.CODE), 
                         expected_nodes)
    
    # Smoke test of all delimiters
    def test_bold_text(self):
        nodes = [
            TextNode(text="This is text with a **bold** word", text_type=TextType.TEXT)
        ]

        expected_nodes = [
            TextNode(text="This is text with a ", text_type=TextType.TEXT),
            TextNode(text="bold", text_type=TextType.BOLD),
            TextNode(text=" word", text_type=TextType.TEXT)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.BOLD.value, TextType.BOLD), 
                         expected_nodes)

    def test_italic_text(self):
        nodes = [
            TextNode(text="This is text with an *italic* word", text_type=TextType.TEXT)
        ]

        expected_nodes = [
            TextNode(text="This is text with an ", text_type=TextType.TEXT),
            TextNode(text="italic", text_type=TextType.ITALIC),
            TextNode(text=" word", text_type=TextType.TEXT)
        ]

        self.assertEqual(split_nodes_delimiter(nodes, DelimiterType.ITALIC.value, TextType.ITALIC), 
                         expected_nodes)
    # link
    # image

    # ## Error Cases

    # # "`bebeb"
    # def test_missing_right_delimiter(self):
    #     raise NotImplementedError

    # # "mytynrrt`"
    # def test_missing_left_delimiter(self):
    #     raise NotImplementedError

    # # "```"
    # def test_only_mismatched_delimiter(self):
    #     raise NotImplementedError

    # # "`"
    # def test_single_delimiter(self):
    #     raise NotImplementedError

