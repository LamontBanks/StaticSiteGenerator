from textnode import *
from htmlnode import *
from parentnode import *
from leafnode import *

def main():

    '''
    Sample transformation

    <div>
        <b>Bold text</b>
        <p style="margin: 15px; line-height: 1.5; text-align: center">
            Normal text
        </p>
        <div>
            <a href="http://www.example.com" target="_blank">My link</a>
            ISO Grocery List
            <ul>
                <li>French Bread</li>
                <li><b>Celery</b></li>
                <li>Milk</li>
            </ul>
            Remember, no <i><b>branded</b></i> products!
        </div>
    </div>
    '''
    node_1 = ParentNode(tag="div",
                        children=[
                            LeafNode(tag="b", value="Bold text"),
                            LeafNode(tag="p", props={ "style": "margin: 15px; line-height: 1.5; text-align: center"}, 
                                     value="Normal text"),
                            ParentNode(tag="div", 
                                       children=[
                                           LeafNode(tag="a", props={"href": "http://www.example.com", "target": "_blank"},
                                                    value="My link"),
                                           LeafNode(value="Grocery List"),
                                           ParentNode(tag="ul",
                                                      children=[
                                                          LeafNode(tag="li", value="French Bread"),
                                                          ParentNode(tag="li",
                                                                     children=[
                                                                         LeafNode(tag="b", value="Celery")
                                                                     ]),
                                                          LeafNode(tag="li", value="Milk"),
                                                      ]),
                                            LeafNode(value="Remember, no "),
                                            ParentNode(tag="i",
                                                       children=[
                                                           ParentNode(tag="b",
                                                                      children=[
                                                                          LeafNode(value="branded")
                                                                      ])
                                                       ]),
                                            LeafNode(value=" products!")
                                        ]
                                    )
                                ]
                            )

    # <div><b>Bold text</b><p style="margin: 15px; line-height: 1.5; text-align: center">Normal text</p><div><a href="http://www.example.com" target="_blank">My link</a>Grocery List<ul><li>French Bread</li><li><b>Celery</b></li><li>Milk</li></ul>Remember, no <i><b>branded</b></i> products!</div></div>
    print(node_1.to_html())


main()
