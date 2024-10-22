from textnode import *
from htmlnode import *

def main():
    dummy_text_node = TextNode("this is my name", "italic", "https://www.boot.dev")
    print(dummy_text_node)

    dummy_html_node = HTMLNode(tag="p", value="text inside a paragraph element", props = { "href": "https://www.google.com" })
    dummy_html_node2 = HTMLNode(tag="p", value="2 text", props = { "href": "https://www.google.com" })
    dummy_html_node3 = HTMLNode(tag="p", value="3 text", props = { "href": "https://www.google.com" }, children = [dummy_html_node, dummy_html_node2])
    
    print(dummy_html_node)
    print(dummy_html_node2)
    print(dummy_html_node3)

main()
