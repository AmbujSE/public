import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestSplitNodesDelimiter(unittest.TestCase):
    
    # def test_basic_split(self):
    #     node = TextNode("This is text with a `code block` word", "text")
    #     result = split_nodes_delimiter([node], "`", "code")
    #     expected = [
    #         TextNode("This is text with a ", "text"),
    #         TextNode("code block", "code"),
    #         TextNode(" word", "text"),
    #     ]
    #     self.assertEqual(result, expected)
    
    # def test_no_delimiter(self):
    #     node = TextNode("This is just plain text", "text")
    #     result = split_nodes_delimiter([node], "`", "code")
    #     expected = [node]
    #     self.assertEqual(result, expected)
    
    # def test_multiple_delimiters(self):
    #     node = TextNode("This is `code1` and `code2` in text", "text")
    #     result = split_nodes_delimiter([node], "`", "code")
    #     expected = [
    #         TextNode("This is ", "text"),
    #         TextNode("code1", "code"),
    #         TextNode(" and ", "text"),
    #         TextNode("code2", "code"),
    #         TextNode(" in text", "text"),
    #     ]
    #     self.assertEqual(result, expected)
    
    # def test_unmatched_delimiter(self):
    #     node = TextNode("This is `unmatched code block text", "text")
    #     with self.assertRaises(ValueError) as context:
    #         split_nodes_delimiter([node], "`", "code")
    #     self.assertTrue("Unmatched delimiter" in str(context.exception))

    # def test_asterisk_delimiter(self):
    #     node = TextNode("This is *italic* text", "text")
    #     result = split_nodes_delimiter([node], "*", "italic")
    #     expected = [
    #         TextNode("This is ", "text"),
    #         TextNode("italic", "italic"),
    #         TextNode(" text", "text"),
    #     ]
    #     self.assertEqual(result, expected)

    # def test_double_asterisk_delimiter(self):
    #     node = TextNode("This is **bold** text", "text")
    #     result = split_nodes_delimiter([node], "**", "bold")
    #     expected = [
    #         TextNode("This is ", "text"),
    #         TextNode("bold", "bold"),
    #         TextNode(" text", "text"),
    #     ]
    #     self.assertEqual(result, expected)

    # def test_mixed_delimiters(self):
    #     node = TextNode("This is *italic* and **bold** text", "text")
    #     result = split_nodes_delimiter([node], "*", "italic")
    #     result = split_nodes_delimiter(result, "**", "bold")
    #     expected = [
    #         TextNode("This is ", "text"),
    #         TextNode("italic", "italic"),
    #         TextNode(" and ", "text"),
    #         TextNode("bold", "bold"),
    #         TextNode(" text", "text"),
    #     ]
    #     self.assertEqual(result, expected)

    # def test_edge_case_empty_text(self):
    #     node = TextNode("", "text")
    #     result = split_nodes_delimiter([node], "`", "code")
    #     expected = [node]
    #     self.assertEqual(result, expected)

    # def test_non_text_node(self):
    #     node = TextNode("Non-text node", "bold")
    #     result = split_nodes_delimiter([node], "`", "code")
    #     expected = [node]
    #     self.assertEqual(result, expected)

    # def test_nested_delimiters(self):
    #     node = TextNode("This is `code with *italic* inside` text", "text")
    #     result = split_nodes_delimiter([node], "`", "code")
    #     result = split_nodes_delimiter(result, "*", "italic")
    #     expected = [
    #         TextNode("This is ", "text"),
    #         TextNode("code with *italic* inside", "code"),
    #         TextNode(" text", "text"),
    #     ]
    #     self.assertEqual(result, expected)
    
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()