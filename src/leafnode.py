from htmlnode import HTMLNode

"""Represents a single HTMLNode with no children

Ex: 
    `<p>This is a paragraph of text.</p>`

The paragraph is a ParentNode, bold tag is the LeafNode:
    `<p>This is a paragraph. <b>This is bold text.</b> This is the last sentence</p>`
"""

class LeafNode(HTMLNode):

    """
        * `tag` - `str` representing the tag name, ex: `"p"` (for `<p>`), `"h1"` (for `<h1>`), required
        * `value` - Required, the value inside the HTML tag, ex: `<h1>This is the value</h1>`, required
        * `props` - dictionary of HTML tag attributes, ex: `{"alt": "this is image alt text", "src": "http://example.com/image.png"}`
    """
    def __init__(self, tag, value, props=None):
        if (value == None):
            raise ValueError(f"Required parameter 'value' not set")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if (self.value == None):
            raise ValueError(f"Required variable 'value' not set")
        
        # If there is no tag, return the value as raw text
        if (self.tag == None):
            return self.value
        
        # Otherwise, return the an HTML tag, ex: <a href="example.com">some link</a>
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"