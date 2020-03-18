class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def insert(node,insnode):
    if node.val==None:
        node=insnode
    if node.val > insnode.val:
        if node.left != None:
            insert(node.left,insnode)
        else:
            node.left = insnode
    elif node.val < insnode.val:
        if node.right != None:
            insert(node.right,insnode)
        else:
            node.right = insnode

def preorder(node):
    print(node.val,end="  ")
    if node.left!=None:
        preorder(node.left)
    if node.right!=None:
        preorder(node.right)

def depth(node):
    if node is None:
        return  0
    else:
        l=depth(node.left)
        r=depth(node.right)
        return l+1 if l>r else r+1

def maxval(node):
    if node.right != None:
        return maxval(node.right)
    else:
        return node.val

def minval(node):
    if node.left != None:
        return maxval(node.left)
    else:
        return node.val

n1=Node(int(input("enter root value:")))
p='y'
while p=='y':
    print("i for insert\n p for print \n d for depth \n h for max value \n l for min value \n e foe exit")
    c=input("ente your choice:\n")
    if c=='i' or c=='I':
        insnode=Node(int(input("enter node to be inserted\n")))
        insert(n1,insnode)
    elif c=='p' or c=='P':
        preorder(n1)
    elif c =='d' or c == 'D':
        print("depth",depth(n1))
    elif c == 'h' or c == 'H':
        print("maxval:",maxval(n1))
    elif c == 'l' or c == 'L':
        print("minval:",minval(n1))
    elif c=='e' or c=='E':
        p='n'
