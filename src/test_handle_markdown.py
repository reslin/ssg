import unittest
from handle_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
    markdown_to_blocks,
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

    def test_no_image_extract(self):
        text = "This is text with a... nothing"
        tuples = extract_markdown_links(text)
        self.assertListEqual(
            [],
            tuples,
        )

    def test_split_nodes_image(self):
        nodes = [
                TextNode("only text", text_type_text),
                TextNode(
                       "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)",
                        text_type_text,
                        )
        ]
        new_nodes = split_nodes_image(nodes)
        #print("result:::::")
        #for node in new_nodes:
        #    print(node)

    def test_split_nodes_link(self):
        nodes = [
                TextNode(
                       "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
                        text_type_text,
                        )
        ]
        new_nodes = split_nodes_link(nodes)
        #print("result:::::")
        #for node in new_nodes:
        #    print(node)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

        new_nodes = text_to_textnodes(text)
        #print("result:::::")
        #for node in new_nodes:
        #    print(node)

    def test_markdown_to_blocks(self):
        text = """This is **bolded** paragraph

           

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        print(markdown_to_blocks(text))