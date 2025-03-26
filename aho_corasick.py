
class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []


def ac_tree_creation(word: str, ac_tree: Node):
    actual = ac_tree
    for letter in word:
        if letter not in actual.children:
            actual.children[letter] = Node()
        actual = actual.children[letter]
    actual.output.append(word)

def build_failure_links(ac_tree: Node):
    queue = []

    for letter, child in ac_tree.children.items():
        child.fail = ac_tree
        queue.append(child)

    while queue:
        current_node = queue.pop(0)
        for letter, child in current_node.children.items():
            fail = current_node.fail

            while fail is not None and letter not in fail.children:
                fail = fail.fail

            if fail and letter in fail.children:
                child.fail = fail.children[letter]
            else:
                child.fail = ac_tree

            child.output += child.fail.output
            queue.append(child)


def patterns_in_text(text: str, ac_tree: Node) -> list:
    results=[]
    current_node=ac_tree

    for index, letter in enumerate(text):
        while letter not in current_node.children and current_node != ac_tree:
            current_node = current_node.fail
        if letter in current_node.children:
            current_node=current_node.children[letter]
        else:
            current_node=ac_tree

        for pattern in current_node.output:
            position=index-len(pattern)+1
            results.append((position, pattern))
    
    return results



"""
TEST
root = Node()
ac_tree_creation("he", root)
ac_tree_creation("she", root)
ac_tree_creation("his", root)
ac_tree_creation("hers", root)

build_failure_links(root)

text = "ushersholisgehe"
print(patterns_in_text(text, root))
"""

