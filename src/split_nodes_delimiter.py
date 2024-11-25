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
            continue

        # Non-matching delimiters
        if len(old_text_split) == 2:
            raise Exception(f"Mismatched {text_type} \"{delimiter}\" delimiter:\n{old_node.text}\n")
        
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

"""Split nodes, similar to split_nodes_delimiter(), but for image Markdown"""
def split_nodes_image(old_nodes):
    # Get matches
    # Recreate markdown
    # Split text, maxsplit=1
    # create nodes for preceding text, images
    # Recursively handle remainining text
    new_nodes = []

    for old_node in old_nodes:
        # Only process TextType.TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Skip empty strings
        if old_node.text == "":
            continue

        # Get image matches
        image_tuples = extract_markdown_images(old_node.text)

        # No matches, add it and move on
        if len(image_tuples) == 0:
            new_nodes.append(old_node)
            continue
        # Otherwise, recreate markdown, and split the text to get the markdown
        else:
            alt_text = image_tuples[0][0]
            src = image_tuples[0][1]
            image_markdown = f"![{alt_text}]({src})"

            old_text_split = old_node.text.split(image_markdown, maxsplit=1)

            # Empty string (somehow)
            if len(old_text_split) == 0:
                continue

            # No split, add node and move on
            if len(old_text_split) == 1:
                new_nodes.append(old_node)
                continue

            # Since we're using the actual markdown as a the delimiter,
            # the string should split into 2 pieces: preceding and remaining text
            if len(old_text_split) == 2:
                preceding_text = old_text_split[0]
                remaining_text = old_text_split[1]

                if preceding_text != "":
                    new_nodes.append(TextNode(text_type=TextType.TEXT, text=preceding_text))

                # Create an IMAGE node
                new_nodes.append(TextNode(text_type=TextType.IMAGE, text=alt_text, url=src))

                if remaining_text != "":
                    remaining_split_nodes = split_nodes_image([TextNode(text_type=TextType.TEXT, text=remaining_text)])
                    if len(remaining_split_nodes) > 0:
                        new_nodes.extend(remaining_split_nodes)
    return new_nodes

"""Split nodes, similar to split_nodes_delimiter(), but for link Markdown.
Could probably refactor into a single method, but will copy-paste for speed"""
def split_nodes_link(old_nodes):
    # Get matches
    # Recreate markdown
    # Split text, maxsplit=1
    # create nodes for preceding text, links
    # Recursively handle remainining text
    new_nodes = []

    for old_node in old_nodes:
        # Only process TextType.TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Skip empty strings
        if old_node.text == "":
            continue

        # Get link matches
        link_tuples = extract_markdown_links(old_node.text)

        # No matches, add it and move on
        if len(link_tuples) == 0:
            new_nodes.append(old_node)
            continue
        # Otherwise, recreate markdown, and split the text to get the markdown
        else:
            link_text = link_tuples[0][0]
            src = link_tuples[0][1]
            link_markdown = f"[{link_text}]({src})"

            old_text_split = old_node.text.split(link_markdown, maxsplit=1)

            # Empty string (somehow)
            if len(old_text_split) == 0:
                continue

            # No split, add node and move on
            if len(old_text_split) == 1:
                new_nodes.append(old_node)
                continue

            # Since we're using the actual markdown as a the delimiter,
            # the string should split into 2 pieces: preceding and remaining text
            if len(old_text_split) == 2:
                preceding_text = old_text_split[0]
                remaining_text = old_text_split[1]

                if preceding_text != "":
                    new_nodes.append(TextNode(text_type=TextType.TEXT, text=preceding_text))

                # Create a LINK node
                new_nodes.append(TextNode(text_type=TextType.LINK, text=link_text, url=src))

                if remaining_text != "":
                    remaining_split_nodes = split_nodes_link([TextNode(text_type=TextType.TEXT, text=remaining_text)])
                    if len(remaining_split_nodes) > 0:
                        new_nodes.extend(remaining_split_nodes)
    return new_nodes


"""Returns a tuple of image inline Markdown, [(<image alt text>, <image source>), (<image alt text>, <image source>), ...]
Helper method for split_nodes_image()
"""
def extract_markdown_images(text):
    # '![image alt text](image src)'
    return re.findall(r"!\[(.+?)\]\((.+?)\)", text)

"""Returns a tuple of link inline Markdown, [(<link>, <link src>), (<link>, <link src>), ...]
Helper method for split_nodes_link()
"""
def extract_markdown_links(text):
    # '[link text](link src)'
    # Regex lookback to avoid capturing image Markdown
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
