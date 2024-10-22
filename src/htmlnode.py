from typing import Optional, List, Dict

class HTMLNode():

    '''
    tag: str
    value: str | int
    children: list of HTMLNodes
    props: dict
    '''
     
    def __init__(
            self, 
            tag = None, 
            value = None, 
            children = None,
            props = None):
        # An HTMLNode without a tag will just render as raw text
        if isinstance(tag, str) or tag == None:
            self.tag = tag

        # An HTMLNode without a value will be assumed to have children
        self.value = value

        # Setting default parameters to [] or {} can have side-effects
        # So, setting the to [] or {} in within the constructor

        # An HTMLNode without children will be assumed to have a value
        # Ensure we at least have an empty list to work with
        self.children = children if children is not None else []

        # An HTMLNode without props simply won't have any attributes
        # Ensure we at least have an empty dictionary to work with
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_props = ""

        for prop, value in self.props.items():
            # Each property must have a *leading space*
            # Also quotes: However, W3C recommends quotes in HTML, and demands quotes for stricter document types like XHTML.
            # https://www.w3schools.com/html/html_attributes.asp
            html_props += f" {prop}=\"{value}\""

        return html_props
    
    def __repr__(self):
        tag_str = f"Tag: {self.tag}"
        value_str = f"Value: {str(self.value)}"
        props_str = f"Properties: {self.props}"
        children_str = f"Children: {self.children}"
        
        return f"HTMLNode({tag_str}, {value_str}, {props_str}, {children_str})"