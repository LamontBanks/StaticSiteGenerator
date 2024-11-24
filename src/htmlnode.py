"""
Represents a node in an HTML document
This class is intended to be inherited

Ex: <p>, <div>, <h1>, <ul><li><li>...</ul>, <img alt="" src="">, etc.
"""
class HTMLNode():

    """Creates an HTML node
        * param `tag` - `str` representing the tag name, ex: `"p"` (for `<p>`), `"h1"` (for `<h1>`)
        * param `value` - the value inside the HTML tag, ex: `<h1>This is the value</h1>`
        * param `children` - list of `HTMLNodes` nested within the tag
        * param `props` - dictionary of HTML tag attributes, ex: `{"alt": "this is image alt text", "src": "http://example.com/image.png"}`

    All parameters are optional (defaults to `None`) - which values are set represent different HTML tag uses:
        - No `tag` - render as raw text
        - No `value` - assumed to have children, ex: `<div>`
        - No `children` - assumed to have a value
        - No `props` - simply won't have no attributes
    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    """Returns the HTML string representation"""
    def to_html(self):
        raise NotImplementedError
    
    """Return the HTML string representation of the HTML attributes
        Ex: 'href="https://www.google.com" target="_blank"'
    """
    def props_to_html(self):
        props_str = ""

        for prop, value in self.props.items():
            # Each property must have a *leading space*
            # Also quotes: However, W3C recommends quotes in HTML, and demands quotes for stricter document types like XHTML.
            # https://www.w3schools.com/html/html_attributes.asp
            props_str += f" {prop}=\"{value}\""

        return props_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})" 
