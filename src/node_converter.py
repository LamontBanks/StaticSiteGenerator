from textnode import *
from leafnode import *
from htmlnode import *

"""Converts a TextNode to an HTML LeafNode
- `TextType.TEXT`: `None` tag, text
- `TextType.BOLD`: "b" tag, text
- `TextType.ITALIC`: "i" tag, text
- `TextType.CODE`: "code" tag, text
- `TextType.LINK`: "a" tag, anchor text, and "href" prop
- `TextType.IMAGE`: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
"""
def text_node_to_html_node(text_node):
    text = text_node.text
    url = text_node.url

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=HTMLTag.TEXT, value=text)
        case TextType.BOLD:
            return LeafNode(tag=HTMLTag.BOLD, value=text)
        case TextType.ITALIC:
            return LeafNode(tag=HTMLTag.ITALIC, value=text)
        case TextType.CODE:
            return LeafNode(tag=HTMLTag.CODE, value=text)
        case TextType.LINK:
            return LeafNode(tag=HTMLTag.LINK, value=text, props={"href": url})
        case TextType.IMAGE:
            return LeafNode(tag=HTMLTag.IMAGE, value="", props={"alt": text, "src": url})
        case _:
            raise Exception(f"Unrecognized TextType: {text_node.text_type}")
        
        