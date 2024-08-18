import unittest

from htmlnode import *

props = {
    "href": "https://www.google.com", 
    "target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_property(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        expected_props = 'href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_multiple_properties(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        expected_props = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_no_properties(self):
        node = HTMLNode(tag="p", value="This is a paragraph")
        expected_props = ""
        self.assertEqual(node.props_to_html(), expected_props)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
            node = HTMLNode(
                "p",
                "What a strange world",
                None,
                {"class": "primary"},
            )
            self.assertEqual(
                node.__repr__(),
                "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
            )

    def test_leafnode_creation_with_value(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        expected_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(leaf.to_html(), expected_html)

    def test_leafnode_creation_with_value_and_props(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        expected_html = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_leafnode_without_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leafnode_with_no_tag_returns_raw_text(self):
        leaf = LeafNode(None, "Just some raw text.")
        expected_html = "Just some raw text."
        self.assertEqual(leaf.to_html(), expected_html)
    
    def test_single_leaf_child(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "This is a paragraph."),
            ]
        )
        expected_html = "<div><p>This is a paragraph.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_multiple_leaf_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "First paragraph."),
                LeafNode("p", "Second paragraph."),
            ]
        )
        expected_html = "<div><p>First paragraph.</p><p>Second paragraph.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text inside paragraph."),
                    ]
                ),
                LeafNode("p", "Second paragraph."),
            ]
        )
        expected_html = "<div><p><b>Bold text inside paragraph.</b></p><p>Second paragraph.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_with_attributes(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "This is a paragraph."),
            ],
            props={"class": "container", "id": "main-div"}
        )
        expected_html = '<div class="container" id="main-div"><p>This is a paragraph.</p></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_empty_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_no_children_provided_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_no_tag_provided_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "This is a paragraph.")])

    def test_nested_with_no_tag_child(self):
        node = ParentNode(
            "div",
            [
                LeafNode(None, "This is just text."),
                LeafNode("p", "This is a paragraph."),
            ]
        )
        expected_html = "<div>This is just text.<p>This is a paragraph.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_deeply_nested_parent_nodes(self):
        node = ParentNode(
            "section",
            [
                ParentNode(
                    "div",
                    [
                        ParentNode(
                            "article",
                            [
                                LeafNode("h1", "Title"),
                                LeafNode("p", "Content of the article."),
                            ]
                        )
                    ]
                )
            ]
        )
        expected_html = "<section><div><article><h1>Title</h1><p>Content of the article.</p></article></div></section>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_with_mixed_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "First paragraph."),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                        LeafNode("li", "Item 3"),
                    ]
                ),
                LeafNode("p", "Second paragraph."),
            ]
        )
        expected_html = "<div><p>First paragraph.</p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><p>Second paragraph.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()