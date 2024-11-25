from textnode import *
from split_nodes_delimiter import *

"""Convert a raw string of markdown-flavored text into a list of TextNode objects.
The order of splitting text matters as some Markdown have similar syntax.

Future improvement: Use regex to find matches and create a single function for splitting 
"""
def text_to_textnodes(text):
    node = TextNode(text=text, text_type=TextType.TEXT)
    
    text_nodes = split_nodes_delimiter([node], TextDelimiter.CODE.value, TextType.CODE)
    
    # Bold before Italic
    text_nodes = split_nodes_delimiter(text_nodes, TextDelimiter.BOLD.value, TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, TextDelimiter.ITALIC.value, TextType.ITALIC)

    # Image before Link
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes