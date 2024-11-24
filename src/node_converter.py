from textnode import *
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
            return HTMLNode(tag=HTMLTag.TEXT, value=text)
        case TextType.BOLD:
            return HTMLNode(tag=HTMLTag.BOLD, value=text)
        case TextType.ITALIC:
            return HTMLNode(tag=HTMLTag.ITALIC, value=text)
        case TextType.CODE:
            return HTMLNode(tag=HTMLTag.CODE, value=text)
        case TextType.LINK:
            return HTMLNode(tag=HTMLTag.LINK, value=text, props={"href": url})
        case TextType.IMAGE:
            return HTMLNode(tag=HTMLTag.IMAGE, value=None, props={"alt": text, "src": url})
        case _:
            raise Exception(f"Unrecognized TextType: {text_node.text_type}")
        
        