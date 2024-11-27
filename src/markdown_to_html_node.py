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
                lines = block.split("\n")
                blockquote_children = []
                # Split, grab text value, add a <br></br> tag between lines
                for line in lines:
                    quote_text = line.split(maxsplit=1)[1]
                    quote_text_html_node = LeafNode(HTMLTag.TEXT, quote_text)
                    br_html_node = LeafNode(HTMLTag.BREAK_ROW, value="")

                    blockquote_children.append(quote_text_html_node)
                    blockquote_children.append(br_html_node)
                # Remove the trailing <br>, if any
                if len(blockquote_children) > 0:
                    blockquote_children.pop()
                # Wrap in <blockquote>
                blockquote_html_node = ParentNode(HTMLTag.BLOCKQUOTE, blockquote_children)
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
            
            # <pre>
            # <code><!-- code --></code>
            # <code><!-- goes --></code>
            # <code><!-- here --></code>
            # <</pre>
            case BlockType.CODE:
                lines = block.split("\n")
                # Remove the leading and trailing "```"
                lines.pop(0)
                lines.pop()

                pre_children = []
                for line in lines:
                    code_html_node = LeafNode(HTMLTag.CODE, line)
                    pre_children.append(code_html_node)
                # Wrap in <pre>
                pre_html_node = ParentNode(HTMLTag.PRE, pre_children)
                html_nodes.append(pre_html_node)

            # Default to raw text in a <p> block
            case _:
                html_nodes.append(LeafNode("p", block))

    # Enclose everything in a <div>
    top_div = ParentNode("div", html_nodes)
    return top_div
