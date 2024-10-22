from htmlnode import HTMLNode

'''
ParentNode class will handle the nesting of HTML nodes inside of one another.
Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.
'''
class ParentNode(HTMLNode):

    '''
    Parent doesn't take a value argument
    The children argument is not optional
    '''
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    '''
    Return a string representing the HTML tag of the node and its children.

    Example:

        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])

        node.to_html()

        ==>

        <p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>
    '''
    def to_html(self):
        if self.tag == None:
            raise ValueError(f"ParentNode `tag` parameter set to {self.tag}, ParentNode `tag` requires a value")
        if self.children == None:
            raise ValueError(f"ParentNode `children` parameter set to {self.children}, ParentNode `children` requires a value")
        
        properties = self.props_to_html()
        opening_tag = f"<{self.tag}{properties}>"
        closing_tag = f"</{self.tag}>"

        html_string = opening_tag
        for child_node in self.children:
            html_string += child_node.to_html()
        html_string += closing_tag

        return html_string
