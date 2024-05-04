import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    split_nodes_delimiter,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_differing_txt_type(self):
        node = TextNode("This is a tuxt node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_inline_bold(self):
        node = TextNode("This is a **bold** node", text_type_text)
        nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" node", text_type_text),
            ],
            nodes,
        )

    def test_inline_italic(self):
        node = TextNode("This is a *italic* node", text_type_text)
        nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" node", text_type_text),
            ],
            nodes,
        )
        


if __name__ == "__main__":
    unittest.main()
