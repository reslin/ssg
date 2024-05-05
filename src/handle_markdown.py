import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for o_node in old_nodes:
        if o_node.text_type != text_type_text:
            new_nodes.append(o_node)
        else:
            separate_textnodes = []
            splitters = o_node.text.split(delimiter)
            if len(splitters) % 2 == 0:
                raise Exception("invalid markdown: opening \"{delimiter}\" not closed")
            for i in range(0, len(splitters)):
                if splitters[i] == "":
                    continue
                if i % 2 == 0:
                    separate_textnodes.append(TextNode(splitters[i], text_type_text))
                else:
                    separate_textnodes.append(TextNode(splitters[i], text_type))
            new_nodes.extend(separate_textnodes)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass