class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def search(node, key):
    if node.val == key:
        return True
    if node.left != None:
        if search(node.left,key):
            return True
    if node.right != None:
        if search(node.right,key):
            return True

n = Node("india")
n1 = Node("south india")
n2 = Node("north india")
n.left=n1
n.right=n2
n1.left = Node("telugu")
n1.right = Node("tamil")
n2.left = Node("hindi")
key = input()
#print(search(n,key))
if search(n, key):
    print("The Searching Node is found in the Tree")
else:
    print("The Searching Node is not found in the Tree")