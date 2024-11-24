"""
Represents inline Markdown text
"""
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():

    """
    param `text` - Text content of the node
    param `text_type` - `TextType` enum
    param `url` - of the link or image, defaults to `None`.
    """
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    
    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type.value == other.text_type.value) and (self.url == other.url)
    

    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"