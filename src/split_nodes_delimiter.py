import functools

from textnode import TextNode, TextType

'''
Convert a raw markdown string into a list of TextNode objects

Markdown parsers often support the nesting of inline elements. For example, you can have a bold word inside of italics:
    This is an *italic and **bold** word*.

However, we will only support a single level of nesting when it comes to inline elements.

Parameters:
    old_nodes - List[TextNode]
    delimiter - str (ex: ` | * | ** )
    text_type - TextType enum, should match the delimiter (ex: "`" and TextType.CODE, "**" and TextType.BOLD)

Example:
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    Returns:
    [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
    ]
'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        # Only handle TextType.TEXT nodes
        # Other nodes (ex: TextType.BOLD, TextType.ITALIC, etc.) don't need parsing
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        else:
            # Proper single (or multiple) delimiter pairs will always split into an array of odd-length of 3 or more
            # If length is even (or somehow 0), the delimiter is mismatched => raise an exception
            split_text = old_node.text.split(delimiter)
            split_text_len = len(split_text)
            
            if split_text_len == 0 or split_text_len % 2 == 0:
                full_text = nodes_combined_text(old_nodes)
                raise Exception(f"Mismatched [{delimiter}] delimiter:\n{full_text}")
            
            # If length = 1, there *are no* delimiters => just add the existing node to the list
            if split_text_len == 1:
                new_nodes.append(old_node)
                continue

            # Add even indices as TextType.TEXT, odd indices as the given text_type
            for i in range(split_text_len):
                text = split_text[i]
                # TextType.TEXT
                if text != "":
                    if i % 2 == 0:
                        new_nodes.append(TextNode(text=text, text_type=TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(text=text, text_type=text_type))

    return new_nodes

def nodes_combined_text(nodes):
    full_text = ""

    for node in nodes:
        full_text += node.text
    
    return full_text
