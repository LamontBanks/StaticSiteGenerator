from markdown_to_textnodes import *
from test_text_node_to_html_node import *
from markdown_blocks import *
from leafnode import *
from parentnode import *

"""Convert a Markdown document toHTMLNodes.
Returns a top-level HTMLNode <div> containing of the nested nodes
"""
def markdown_to_html_node(markdown):
    html_nodes = []

    # Split by block, create HTMLNodes
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            # Normal text: Wrap inline Markdown in <p>
            case BlockType.NORMAL:
                text_nodes = text_to_textnodes(block)
                p_children = []
                # Convert each TextNode to an HTMLNode, add to <p> children
                for text_node in text_nodes:
                    text_html_node = text_node_to_html_node(text_node)
                    p_children.append(text_html_node)
                # Wrap in <p> 
                p_html_node = ParentNode("p", p_children)
                html_nodes.append(p_html_node)

            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                ol_children = []
                # Split the list item (once) between the numbering and text
                # Grab the text, create a leafnode, add to <ol> children
                for line in lines:
                    # List Item format:
                    #   123. item text
                    list_item_text = line.split(maxsplit=1)[1]
                    list_item_html_node = LeafNode(HTMLTag.LIST_ITEM, list_item_text)
                    ol_children.append(list_item_html_node)
                # Wrap in <ol>
                ol_html_node = ParentNode(HTMLTag.ORDERED_LIST, ol_children)
                html_nodes.append(ol_html_node)

            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                ul_children = []
                # Split the list item (once) between the (*/-) symbol and text
                # Grab the text, create a leafnode, add to <ul> children
                for line in lines:
                    # List Item format:
                    #   - item text or * item text
                    list_item_text = line.split(maxsplit=1)[1]
                    list_item_html_node = LeafNode(HTMLTag.LIST_ITEM, list_item_text)
                    ul_children.append(list_item_html_node)
                # Wrap in <ul>
                ul_html_node = ParentNode(HTMLTag.UNORDERED_LIST, ul_children)
                html_nodes.append(ul_html_node)

            case BlockType.QUOTE:
                # Split to get the quote text, but recombine into single quote string (with newlines)
                # Wrap entire string in <blockquote>
                lines = block.split("\n")
                raw_quote_string = ""
                for line in lines:
                    quote_text = line.split(maxsplit=1)[1]
                    raw_quote_string += quote_text + "\n"
                raw_quote_string = raw_quote_string.strip()

                # Wrap in <blockquote>
                blockquote_html_node = LeafNode(HTMLTag.BLOCKQUOTE, raw_quote_string)
                html_nodes.append(blockquote_html_node)

            case BlockType.HEADING:
                lines = block.split("\n")
                # Count the number of #'s, set the appropriate tag (or default to plain text)
                for line in lines:
                    pound_symbols, header_text = line.split(maxsplit=1)[:2]
                    pound_symbol_count = len(pound_symbols)

                    heading_tag = ""
                    match pound_symbol_count:
                        case 1:
                            heading_tag = HTMLTag.HEADING_1
                        case 2:
                            heading_tag = HTMLTag.HEADING_2
                        case 3:
                            heading_tag = HTMLTag.HEADING_3
                        case 4:
                            heading_tag = HTMLTag.HEADING_4
                        case 5:
                            heading_tag = HTMLTag.HEADING_5
                        case 6:
                            heading_tag = HTMLTag.HEADING_6
                        case _:
                            heading_tag = HTMLTag.TEXT
                    # Create header tag
                    heading_html_node = LeafNode(heading_tag, header_text)
                    html_nodes.append(heading_html_node)
            
            # <pre><code>hello()\nworld()</code></pre>
            case BlockType.CODE:
                # Skip the leading and trailing "```", and recombine the raw code line with newlines
                lines = block.split("\n")
                raw_code_string = ""
                for i in range(1, len(lines) - 1):
                    raw_code_string += lines[i] + "\n"
                raw_code_string = raw_code_string.strip()

                # Wrap raw code in <code>, then in <pre>
                code_html_node = LeafNode(HTMLTag.CODE, raw_code_string) 
                pre_html_node = ParentNode(HTMLTag.PRE, [code_html_node])
                html_nodes.append(pre_html_node)

            # Default to raw text in a <p> block
            case _:
                html_nodes.append(LeafNode("p", block))

    # Enclose everything in a <div>
    top_div = ParentNode("div", html_nodes)
    return top_div

"""Returns the title of the Markdown doc
Title should be an H1 line at the start of the document, ex:

# This is the Title

Other content comes after

- item 1
- item 2

## Some other header

```code()```

=> This is the Title
# TODO: Put Markdown syntax into a clas/enum
"""
def extract_title(markdown):
    markdown = markdown.strip()
    if markdown.startswith(f"# "):
        # '# Title' => ['', 'Title'] => Title
        title = markdown.split('\n\n')[0].split(f"# ")[1]
        return title.strip()
    else:
        raise Exception("Markdown document must start with an H1 line")