import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "text in paragraph", None, None)
        node2 = HTMLNode("p", "text in paragraph", None, None)
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("p", "text in paragraph", None, props)
        self.assertEqual(node.props_to_html(),
                         " href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_leafnode_paragraph(self):
        lnode = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(lnode.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode_with_props(self):
        lnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(lnode2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leafnode_no_tag(self):
        lnode = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(lnode.to_html(), "This is a paragraph of text.")

    def test_parentnode(self):
        ln1 = LeafNode("i", "blabla")
        ln2 = LeafNode("b", "blublu")
        pnode2 = ParentNode("p", [ln2,])
        pnode = ParentNode("p", [pnode2, ln1,])
        self.assertEqual(pnode.to_html(), "<p><p><b>blublu</b></p><i>blabla</i></p>")
        #print(pnode.to_html())

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()