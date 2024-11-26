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
