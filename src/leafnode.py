from htmlnode import *

'''
A LeafNode is a type of HTMLNode that represents a single HTML tag with no children.

For example, a simple <p> tag with some text inside of it:
    <p>This is a paragraph of text.</p>

We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. It's a node with no children.

In this next example, <p> is not a leaf node, but <b> is:
    <p>This is a paragraph. <b>This is bold text.</b> This is the last sentence</p>
'''
class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        if (value == None):
            raise ValueError(f"LeafNode's value parameter = {value}. LeafNode *must* have a value set")

        super().__init__(tag=tag, value=value, props=props)

    '''
    Renders a leaf node as an HTML string
    If there is no tag (e.g. it's None), the value should be returned as raw text.
    If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.

    Examples:
        LeafNode("p", "This is a paragraph of text.")
        <p>This is a paragraph of text.</p>

        LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        <a href="https://www.google.com">Click me!</a>

        LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        Click me!

        LeafNode("a", None, {"href": "https://www.google.com"})
        ValueError
    '''
    def to_html(self):
        if (self.value == None):
            raise ValueError(f"LeafNode's value parameter = {self.value}. LeafNode *must* have a value set")

        if (self.tag == None):
            return self.value
        else:
            properties = self.props_to_html()
            opening_tag = f"<{self.tag}{properties}>"
            closing_tag = f"</{self.tag}>"
            
            return f"{opening_tag}{self.value}{closing_tag}"
