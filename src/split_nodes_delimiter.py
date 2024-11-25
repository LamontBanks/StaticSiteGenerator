import re
from textnode import *

"""
Convert a `list` of TextNodes where Markdown words are split, and converted into the specified TextType.

- param old_nodes - `list` of TextNodes
- param delimiter - `str` Markdown delimiter

Ex:
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    Returns:
    [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
    ]

Does not support nested Markdown
Given delimiters like bold ("**") and italics ("*") are similar, the order of calling this function will affect the correctness of output
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # If a Markdown is properly delimited, the string will always maxsplit=2 into *3* strings on the delimiter
    #
    # Ex:
    # No delimiters, not properly delimited, or empty string:
    # 'Here is some text.'.split("`", maxsplit=2)                  => ['Here is some text.']
    # ''.split("`", maxsplit=2)                                    => []
    # 'Here is some wrong `code Markdown'.split("`", maxsplit=2)   => ['Here is some wrong ', 'code ', 'Markdown`'] # Processing will start ok, but fail on 'Markdown`"` 
    #
    # Proper Markdown:
    # 'Here is some `code` Markdown'.split("`", maxsplit=2)     => ['Here is some ', 'code', ' Markdown']
    # 'Here is some Markdown `code`'.split("`", maxsplit=2)     => ['Here is some Markdown', 'code', '']   # Empty string after
    # '`Code` is proper Markdown'.split("`", maxsplit=2)        => ['', 'Code', ' is proper Markdown']     # Empty string beofre
    # '`code`'.split("`", maxsplit=2)                           => ['', 'code', '']                        # Empty string before and after

    # Steps:
    # Split the string once to find the first match
    # Add the first string as a TextType.TEXT node to the new_nodes
    # Then, add the second string as the specific TextType (Ex: TextType.CODE)
    # Finally, pass the final string into this function recursively
    # Extend new_nodes with the recursive output
    new_nodes = []
    for old_node in old_nodes:
        # Only process TextType.TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Skip empty strings
        if old_node.text == "":
            continue

        # Split by delimiter
        old_text_split = old_node.text.split(delimiter, maxsplit=2)

        # Empty string (somehow)
        if len(old_text_split) == 0:
            continue

        # No split, add node and move on
        if len(old_text_split) == 1:
            new_nodes.append(old_node)

        # Non-matching delimiters
        if len(old_text_split) == 2:
            raise Exception(f"Mismatched delimiters: {old_node.text}")
        
        # Process text into TextNodes
        if len(old_text_split) == 3:
            preceding_text = old_text_split[0]
            delimited_text = old_text_split[1]
            remaining_text = old_text_split[2]

            if preceding_text != "":
                new_nodes.append(TextNode(text_type=TextType.TEXT, text=preceding_text))

            if delimited_text != "":
                new_nodes.append(TextNode(text_type=text_type, text=delimited_text))

            if remaining_text != "":
                remaining_split_nodes = split_nodes_delimiter([TextNode(text_type=TextType.TEXT, text=remaining_text)],
                                                              delimiter,
                                                              text_type)
                if len(remaining_split_nodes) > 0:
                    new_nodes.extend(remaining_split_nodes)
        
    return new_nodes

"""Returns a tuple of image inline Markdown, (<image alt text>, <image source>)
"""
def extract_markdown_images(text):
    # '![image alt text](image src)'
    return re.findall(r"!\[(.+?)\]\((.+?)\)", text)

print(extract_markdown_images('This is an ![image alt text](https://i.imgur.com/aKaOqIh.gif) and ![blah](https://i.imgur.com/1234.gif) vwrb3pom3'))
print(extract_markdown_images('vebrb ![eqge vrwev](https://i.imgur.com/aKaOqIh.gif)'))