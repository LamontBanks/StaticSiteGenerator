from enum import Enum

class TextType(Enum):
    TEXT = "text"
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class DelimiterType(Enum):
    TEXT = " "
    ITALIC = '*'
    BOLD = '**'
    CODE = '`'
    LINK = ""   # TODO      [custom text](www.example.com)
    IMAGE = ""  # TODO      [alt text](/src/images/image.png)

class TextNode():

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_text_node):
        return (self.text == other_text_node.text) and (self.text_type == other_text_node.text_type) and (self.url == other_text_node.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
