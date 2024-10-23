from leafnode import LeafNode
from textnode import TextType

'''
Convert TextNode to HTML Node, based on the TextNode ty[e]:

TextType.TEXT: This should become a LeafNode with no tag, just a raw text value.
TextType.BOLD: This should become a LeafNode with a "b" tag and the text
TextType.ITALIC: "i" tag, text
TextType.CODE: "code" tag, text
TextType.LINK: "a" tag, anchor text, and "href" prop
TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)

If none of these types, raises an Exception.
'''
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            href = text_node.url if text_node.url is not None else ""
            return LeafNode(tag="a", value=text_node.text, props={ "href": href })
        case TextType.IMAGE:
            src = text_node.url if text_node.url is not None else ""
            alt = text_node.text if text_node.text is not None else ""
            return LeafNode(tag="img", value="", props={ "src": src, "alt": alt })
        case _:
            raise Exception(f"Not a valid TextType: {text_node.text_type}")
