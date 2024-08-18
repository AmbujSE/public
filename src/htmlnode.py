class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f'{key}="{value}" '
        return result.strip()
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children!r}, {self.props!r})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value  # Return the raw text if there's no tag
        props_str = self.props_to_html()
        if props_str == "":
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children is None or len(children) == 0:
            raise ValueError("ParentNode must have children.")
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if self.children is None:
            return ValueError("ParentNode must have children.")
        props_str = self.props_to_html()
        children_html = ''.join(map(lambda child: child.to_html(), self.children))
        if props_str == "":
            return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
        return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"

props = {
    "href": "https://www.google.com", 
    "target": "_blank",
}

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)


print(node.to_html())

def main():
    HTML_node = HTMLNode("p", "This is a paragraph", children=[], props=props)
    print(HTML_node)
    print(HTML_node.props_to_html())

if __name__ == "__main__":
    main()
