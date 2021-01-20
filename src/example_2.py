# LINKED LIST STACK

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({self.value})"

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        cur = self.head
        result = ''

        while cur is not None:
            result += str(cur.value)
            if cur.next is not None:
                result += ' -> '
            cur = cur.next
        return result
    
    def add_to_head(self, n):
        # set next on new node to old head
        n.next = self.head

        # set head of list to new node
        self.head = n

    def del_from_head(self):
        if self.head is None:
            return None
        
        old_head = self.head
        self.head = self.head.next

        old_head.next = None
        return old_head
    
    def push(self, n):
        self.add_to_head(n)
    
    def pop(self):
        return self.del_from_head()
    
    def find_tail(self):
        if self.head is None:
            return None
        prev = None
        cur = self.head

        while cur.next is not None:
            prev = cur
            cur = cur.next
        
        return (prev, cur)

    def enqueue(self, n):
        self.add_to_head(n)
    
    def dequeue(self):
        prev, tail = self.find_tail()
        if prev is not None:
            # dequeue the head
            self.head = None
        else:
            prev.next = None
        return tail

    # PUSH a new item on a stack
    # POP an existing item off a stack

a = ListNode(12)
b = ListNode(24)
c = ListNode(48)
d = ListNode(96)


a.next = b
b.next = c
c.next = d
d.next = None

head = a

ll = LinkedList(head)
ll2 = LinkedList()

print(ll)

ll2.add_to_head(ListNode(222))
print(ll2)

old_node = ll2.del_from_head()
print(ll2)
print(old_node)

# PUSH / POP (LIFO)
ll3 = LinkedList()

ll3.push(ListNode(11))
ll3.push(ListNode(22))
ll3.push(ListNode(33))
ll3.push(ListNode(44))

print(ll3)

last = ll3.pop()
print(last)

# ENQUEUE / DEQUEUE (FIFO)
ll4 = LinkedList()

ll4.enqueue(ListNode(11))
ll4.enqueue(ListNode(22))
ll4.enqueue(ListNode(33))
ll4.enqueue(ListNode(44))

print(ll4)

last = ll4.dequeue()
print(last)

print(ll4)
