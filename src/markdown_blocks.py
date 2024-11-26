from enum import Enum

class BlockType(Enum):
    NORMAL = "normal"
    CODE = "code"
    QUOTE = "quote"
    HEADING = "heading"
    ORDERED_LIST = "ordered list"
    UNORDERED_LIST = "unordered_list"

"""Split Markdown text into text blocks.

Blocks are seperated by blank lines
Current limitation: Code blocks cannot have blank lines
"""
def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    final_blocks = []

    # Strip whitespace from ends of each block
    for block in blocks:
        block = block.lstrip().rstrip()

        if block != "":
            final_blocks.append(block)

    return final_blocks


"""Determine the "type" of a Markdown block based on block delimiters.
We will Supports 6 types of markdown blocks:
    - paragraph
    - heading
    - code
    - quote
    - unordered_list
    - ordered_list

Assumes valid/proper Markdown and that Markdown blocks are coming from `markdown_to_blocks()`
"""
def block_to_block_type(block):
    # Headings, h1 to h6
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    # Code block, starts with ```, ends with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Quote block, every line must start with "> "
    if is_quote_block(block):
        return BlockType.QUOTE
    
    # Unordered list, every line starts with "- " or "* "
    if is_unordered_list_block(block):
        return BlockType.UNORDERED_LIST
    
    # Ordered list, each line starts with a number, and increments starting from 1. to whatever
    # Ex:
    #   1. Item one
    #   2. Item two
    #   3. Item three
    if is_ordered_list_block(block):
        return BlockType.ORDERED_LIST
    
    # If nothing matches, it's a normal paragraph
    return BlockType.NORMAL


# Helper functions

def is_quote_block(block):
    lines = block.split("\n")
    if len(lines) == 0:
        return False
    for line in lines:
        if not line.startswith("> "):
            return False
    # If everything passes, it a quote block
    return True

def is_unordered_list_block(block):
    lines = block.split("\n")
    if len(lines) == 0:
        return False
    for line in lines:
        if not line.startswith("- ") and not line.startswith("* "):
            return False
    # If everything passes, it a unordered list block
    return True

def is_ordered_list_block(block):
    lines = block.split("\n")
    if len(lines) == 0:
        return False
    for i in range(len(lines)):
        # Check that each line starts with 1. , 2. , etc.
        if not lines[i].startswith(f"{i + 1}. "):
            return False
    # If everything passes, it a ordered list block
    return True
