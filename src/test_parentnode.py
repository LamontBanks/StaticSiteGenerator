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

    """
    HTML:

    <div>
        <b>Bold text</b>
        <p style="margin: 15px; line-height: 1.5; text-align: center">
            Centered text
        </p>
        <div>
            <a href="http://www.example.com" target="_blank">My link</a>
            <p>
                ISO Grocery List
                <br></br>
                <ul>
                    <li>French Bread</li>
                    <li>Celery</li>
                    <li>Milk</li>
                </ul>
                Remember, no <b>branded</b> products!
            </p>
        </div>
    </div>
    """
    def test_to_html(self):
        html_nodes = ParentNode(tag="div", children=[
            LeafNode(tag="b", value="Bold text"),
            ParentNode(tag="p", props={ "style": "margin: 15px; line-height: 1.5; text-align: center"}, children=[
                LeafNode(tag=None, value="Centered text"),
            ]),
            ParentNode(tag="div", children=[
                LeafNode(tag="a", props={"href": "http://www.example.com", "target": "_blank"}, value="My link"),
                ParentNode(tag="p", children=[
                    LeafNode(tag=None, value="ISO Grocery List"),
                    LeafNode(tag="br", value=""),
                    ParentNode(tag="ul", children=[
                        LeafNode(tag="li", value="French Bread"),
                        LeafNode(tag="li", value="Celery"),
                        LeafNode(tag="li", value="Milk")
                    ]),
                    LeafNode(tag=None, value="Remember, no "),
                    LeafNode(tag="b", value="branded"),
                    LeafNode(tag=None, value=" products!")
                ]),
            ])
        ])

        raw_html = '<div><b>Bold text</b><p style="margin: 15px; line-height: 1.5; text-align: center">Centered text</p><div><a href="http://www.example.com" target="_blank">My link</a><p>ISO Grocery List<br></br><ul><li>French Bread</li><li>Celery</li><li>Milk</li></ul>Remember, no <b>branded</b> products!</p></div></div>'
        self.assertEqual(html_nodes.to_html(), raw_html)

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