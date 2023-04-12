# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/10 13:34
# @File    : treeStruct.py
from anytree import Node, RenderTree

root = Node("root")


def tree_from_given_title(title_list, add_layer_data):
    dic = {}
    count = 0
    for i in title_list:
        count += 1
        dic['[MOVIE{}] '.format(count) + i] = add_layer_data[i]
    return dic


def parse_data(parent, data):
    if isinstance(data, dict):
        for key, value in data.items():
            node = Node(f"{key}: ", parent=parent)
            parse_data(node, value)
    elif isinstance(data, list):
        for i, value in enumerate(data):
            node = Node(f"[{i}]: ", parent=parent)
            parse_data(node, value)
    else:
        parent.name += str(data)


def print_tree(title_list, add_layer_data):
    get_data = tree_from_given_title(title_list, add_layer_data)
    parse_data(root, get_data)
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
