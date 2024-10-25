import unittest
from markdown_to_textnode import split_nodes_delimiter
from textnode import TextNode, TextType, DelimiterType

class TestMarkdownToTextNode(unittest.TestCase):
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
            TextNode(text="Green functions: `.reduce()`, `.reuse()`, and `.recycle()`.", text_type=TextType.TEXT),
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

    def test_mixed_words(self):
        # Delimited, empty strings will not generate nodes
        nodes = [
            TextNode(text="`code1`plain1`code2` plain2 `code3``code4  ` `` plain3 `` plain4 `` ``", text_type=TextType.TEXT),
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



    # # ""
    # def test_empty_string(self):
    #     raise NotImplementedError

    # # " `` ` ` `` ` ` `` `````` ` `"
    # def test_only_delimiters(self):
    #     raise NotImplementedError

    # # "code"
    # def test_plain_text(self):
    #     raise NotImplementedError
    
    # ## Testing deliminters

    # # Text
    # # Code
    # # Bold
    # # Italics
    # # link

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

