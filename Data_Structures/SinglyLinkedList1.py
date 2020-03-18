class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
def printLinkedList(head):
    if head == None:
        return
    while head != None:
        print(head.data)
        head = head.next

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    temp = head
    i = 1
    while i < position:
        temp = temp.next
        i += 1
    new_node.next = temp.next
    temp.next = new_node
    return head

def deleteNode(head, position):
    temp = head
    if position == 0:
        return head.next
    i = 0
    while i < position-1:
        temp = temp.next
        i += 1
    temp.next = temp.next.next
    return head

def reverse(head):
    p = head
    q = p.next
    if q == None:
        return p
    q = reverse(q)
    p.next.next = p
    p.next = None
    return q

def getNode(head, positionFromTail):
    tailing_node = head
    length = 0
    while head:
        if length > positionFromTail:
            tailing_node = tailing_node.next
        head = head.next
        length += 1
    return tailing_node.data

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
    insertNodeAtPosition(llist.head, 20, 3)
    printLinkedList(llist.head)
    deleteNode(llist.head, 2)
    printLinkedList(llist.head)
    reverse(llist.head)
    printLinkedList(llist.head)
    print(getNode(llist.head, positionFromTail = 2))