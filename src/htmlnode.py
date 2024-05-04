class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for k, v in self.props.items():
            html += f" {k}=\"{v}\""
        return html
    
    def __eq__(self, other):
        if (self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props):
            return True
        return False
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("missing value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        if (self.tag == other.tag
            and self.value == other.value
            and self.props == other.props):
            return True
        return False

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag missing")        
        if self.children == None:
            raise ValueError("children missing")
        
        html = ""
        for child in self.children:
            html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"

    def __eq__(self, other):
        if (self.tag == other.tag
            and self.value == other.value
            and self.props == other.props):
            return True
        return False

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"