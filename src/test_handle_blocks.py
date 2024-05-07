import unittest
from handle_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from handle_blocks import (
    markdown_to_blocks,
    block_to_block_type
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestHandleBlocks(unittest.TestCase):
    
    def test_heading(self):
        text = "###### heading6"
        self.assertEqual(block_to_block_type(text), "heading")

    def test_code(self):
        text = "``` code```"
        self.assertEqual(block_to_block_type(text), "code")

    def test_quote(self):
        text = ">abc\n>def"
        self.assertEqual(block_to_block_type(text), "quote")

    def test_ulist(self):
        text = "- abc\n- def"
        self.assertEqual(block_to_block_type(text), "unordered_list")

    def test_olist(self):
        text = "1. abc\n. def"
        self.assertEqual(block_to_block_type(text), "ordered_list")

    def test_markdown_to_blocks(self):
        text = """This is **bolded** paragraph

           

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        #print(markdown_to_blocks(text))



if __name__ == "__main__":
    unittest.main()