import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
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
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text) #returns list of tuples

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text) #returns list of tuples

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if "![" in node.text:
            node_tuples = extract_markdown_images(node.text)
            splitters = node.text.split(f"![{node_tuples[0][0]}]({node_tuples[0][1]})")
            if splitters[0] != "":
                new_nodes.append(TextNode(splitters[0], text_type_text))
            new_nodes.append(TextNode(node_tuples[0][0], text_type_image, node_tuples[0][1]))
            if len(splitters) > 1 and splitters[1] != "":
                new_nodes.extend(split_nodes_image([TextNode(splitters[1], text_type_text)]))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if "[" in node.text:
            node_tuples = extract_markdown_links(node.text)
            splitters = node.text.split(f"[{node_tuples[0][0]}]({node_tuples[0][1]})")
            if splitters[0] != "":
                new_nodes.append(TextNode(splitters[0], text_type_text))
            new_nodes.append(TextNode(node_tuples[0][0], text_type_link, node_tuples[0][1]))
            if len(splitters) > 1 and splitters[1] != "":
                new_nodes.extend(split_nodes_link([TextNode(splitters[1], text_type_text)]))
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, text_type_text)], "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes