import re

from handle_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import (
    LeafNode,
    ParentNode,
)

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


#re_code_start = r"^`{3}"
#re_code_end = r"`{3}$"
re_heading = r"^#{1,6}\s+\w+"
#re_ulist = r"^[*-]{1}\s+"
re_olist = r"[0-9]\.+\s+"

def markdown_to_blocks(markdown):
    blocks = []
    splitters = markdown.split("\n\n")
    for splitter in splitters:
        s = splitter.strip()
        if s != "":
            blocks.append(s)
    return blocks

def block_to_block_type(markdown):
    if re.match(re_heading, markdown):
        return block_type_heading
    if markdown.startswith("```") and markdown.endswith("```"):
        return block_type_code
    if markdown.startswith(">"):
        is_quote = True
        splitters = markdown.split("\n")
        for splitter in splitters:
            if not splitter.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return block_type_quote
    if markdown.startswith("* "):
        is_ulist = True
        splitters = markdown.split("\n")
        for splitter in splitters:
            if not splitter.startswith("* "):
                is_ulist = False
                break
        if is_ulist:
            return block_type_ulist  
    if markdown.startswith("- "):
        is_ulist = True
        splitters = markdown.split("\n")
        for splitter in splitters:
            if not splitter.startswith("- "):
                is_ulist = False
                break
        if is_ulist:
            return block_type_ulist
    if re.match(re_olist, markdown):
        is_olist = True
        splitters = markdown.split(".", 1)
        if splitters[0] != "1":
            is_olist = False
        if is_olist:
            num = 1
            lines = markdown.split("\n")
            for line in lines:
                numbers = line.split(".", 1)
                if not numbers[0].isdigit() or int(numbers[0]) != num:
                    is_olist = False
                    break
                num = int(numbers[0]) + 1
        if is_olist:
            return block_type_olist
    return block_type_paragraph

def text_to_nodes(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def block_quote_to_html_node(block):
    nodes = text_to_nodes("\n".join(map(lambda l: l.lstrip(">"), block.split("\n"))))
    return ParentNode("blockquote", nodes)

def block_ulist_to_html_node(block):
    items = block.split("\n")
    li_nodes = []
    for item in items:
        stext = item[2:]
        children = text_to_nodes(stext)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ul", li_nodes)

def block_olist_to_html_node(block):
    items = block.split("\n")
    li_nodes = []
    for item in items:
        stext = item[3:]
        children = text_to_nodes(stext)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ol", li_nodes)

def block_code_to_html_node(block):
    nodes = text_to_nodes(block.strip("`"))
    code_node = ParentNode("code", nodes)
    return ParentNode("pre", [code_node])

def block_heading_to_html_node(block):
    splitters = block.split(" ", 1)
    heading_level = len(splitters[0])
    nodes = text_to_nodes(block.lstrip("# "))
    return ParentNode(f"h{heading_level}", nodes)

def block_paragraph_to_html_node(block):
    nodes = text_to_nodes(block)
    return ParentNode("p", nodes)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            nodes.append(block_heading_to_html_node(block))
        elif block_to_block_type(block) == block_type_code:
            nodes.append(block_code_to_html_node(block))
        elif block_to_block_type(block) == block_type_quote:
            nodes.append(block_quote_to_html_node(block))
        elif block_to_block_type(block) == block_type_ulist:
            nodes.append(block_ulist_to_html_node(block))
        elif block_to_block_type(block) == block_type_olist:
            nodes.append(block_olist_to_html_node(block))
        else:
            nodes.append(block_paragraph_to_html_node(block))
    return ParentNode("div", nodes)