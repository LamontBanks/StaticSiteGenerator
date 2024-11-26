from htmlnode import *

"""Represents an HTMLNode with children

Ex: <ul> is a ParentNode, <li> are LeafNodes:
    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ol>
"""
class ParentNode(HTMLNode):

    """
        - tag - HTML tag `str`, required
        - children - `list` of HTMLNodes, required
        - props - `dict` of HTML attributes
    """
    def __init__(self, tag, children, props=None):
        if (tag == None):
            raise ValueError(f"Required parameter 'tag' not set")
        if (children == None):
            raise ValueError(f"Required parameter 'children' not set")
        
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if (self.tag == None):
            raise ValueError(f"Required variable 'tag' not set")
        if (self.children == None):
            raise ValueError(f"Required variable 'children' not set")
        
        properties = self.props_to_html()
        opening_tag = f"<{self.tag}{properties}>"
        closing_tag = f"</{self.tag}>"

        html_string = opening_tag
        for child_node in self.children:
            html_string += child_node.to_html()
        html_string += closing_tag

        return html_string
