# from textnode import (
#     TextNode,
# )

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []

#     for node in old_nodes:
#         if node.text_type != "text":
#             new_nodes.append(node)
#             continue

#     parts = node.text.split(delimiter)

#     # Check for unmatched delimiter (i.e., an odd number of parts)
#     if len(parts) % 2 == 0:
#         raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

#     for i, part in enumerate(parts):
#         if i % 2 == 0:
#             # Outside delimiter, keep as text
#             if part:
#                 new_nodes.append(TextNode(part, "text"))
#         else:
#             # Inside delimiter, apply the given text_type
#             new_nodes.append(TextNode(part, text_type))

#     return new_nodes

# node = TextNode("This is text with a `code block` word", "text")
# new_nodes = split_nodes_delimiter([node], "`", "code")

# print(new_nodes)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
