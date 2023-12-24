def minimax_alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        value = float('-inf')
        for child in node.get_children():
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.get_children():
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def is_terminal(self):
        return len(self.children) == 0

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children
    

root = Node(3)
node1 = Node(5)
node2 = Node(2)
node3 = Node(9)
node4 = Node(8)
node5 = Node(1)
node6 = Node(4)

root.children = [node1, node2]
node1.children = [node3, node4]
node2.children = [node5, node6]

# Set the depth and initial alpha and beta values
depth = 3
alpha = float('-inf')
beta = float('inf')

# Call the minimax_alpha_beta function
result = minimax_alpha_beta(root, depth, alpha, beta, True)
print(result)