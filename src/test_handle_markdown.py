import unittest
from handle_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestHandleMarkdown(unittest.TestCase):
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

    def test_inline_double_code(self):
        node = TextNode("This is a `code1` and `code2` node", text_type_text)
        nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("code1", text_type_code),
                TextNode(" and ", text_type_text),
                TextNode("code2", text_type_code),
                TextNode(" node", text_type_text),
            ],
            nodes,
        )
        
    def test_extract_image(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        tuples = extract_markdown_images(text)
        self.assertListEqual(
            [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"),
            ],
            tuples,
        )

    def test_extract_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        tuples = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
            tuples,
        )
    # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]