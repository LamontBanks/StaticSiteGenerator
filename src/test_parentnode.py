import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    # "Full" test" LeafNodes (tag, no tag, props, no props), nested ParentNodes
    # Nest ParentNodes - 3 levels
    # Multiple same-level ParentNodes
    # ParentNode + 3 leafnodes
    def test_parent_node_full(self):
        # Remove char limit in diff shown failed assertions
        self.maxDiff = None

        '''
        Original HTML:

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
        node = ParentNode(tag="div",
                        children=[
                            LeafNode(tag="b", value="Bold text"),
                            LeafNode(tag="p", props={ "style": "margin: 15px; line-height: 1.5; text-align: center"}, 
                                     value="Normal text"),
                            ParentNode(tag="div", 
                                       children=[
                                           LeafNode(tag="a", props={"href": "http://www.example.com", "target": "_blank"},
                                                    value="My link"),
                                           LeafNode(value="ISO Grocery List"),
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
        
        self.assertEqual(node.to_html(), '<div><b>Bold text</b><p style="margin: 15px; line-height: 1.5; text-align: center">Normal text</p><div><a href="http://www.example.com" target="_blank">My link</a>ISO Grocery List<ul><li>French Bread</li><li><b>Celery</b></li><li>Milk</li></ul>Remember, no <i><b>branded</b></i> products!</div></div>')

    # ParentNode - Empty children ("no" children)
    def test_parent_node_no_children(self):
        parent_node = ParentNode(tag="div", children = [])
        self.assertEqual(parent_node.to_html(), '<div></div>')
    
    # ParentNode + 1 leafnode
    def test_parent_node_single_leaf_node(self):
        parent_node = ParentNode(tag="p", children=[
            LeafNode(tag="a", props={"href": 'http://www.example.com'}, 
                     value="Link to example.com")
        ])

        self.assertEqual(parent_node.to_html(), '<p><a href="http://www.example.com">Link to example.com</a></p>')

    # Error: ParentNode with None children
    def test_parent_node_none_children(self):
        parent_node = ParentNode(tag="div", children=[])
        parent_node.children = None

        with self.assertRaises(ValueError):
            parent_node.to_html()

    # Error: ParentNode with no tag
    def test_parent_with_no_tag(self):
        parent_node = ParentNode(tag="div", children=[])
        parent_node.tag = None

        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()