import re
from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Unknown text type")
    
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