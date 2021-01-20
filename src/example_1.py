class Node:
    # find me!
    def __init__(self, val, nxt=None):
        self.value = val
        self.next = nxt

    def __repr__(self):
        return f'Node({repr(self.value)})'

head = None

def insert_at_front(val):
    global head

    # make a new node
    new_node = Node(val)

    # point new head next at head
    new_node.next = head

    # point head to new node
    head = new_node

def print_list():
    global head

    # set cur to head
    cur = head

    # loop while cur.next is not None
    while cur is not None:
        # print value at cur
        print(cur.value)

        # set cur to cur.next
        cur = cur.next

def delete_head():
    global head

    # old head will be garbage cleaned, so this is optional
    old_next = head.next
    head.next = None

    # point head to head.next (if above is commented out, head.next)
    head = old_next

def delete_node(value):
    global head
    
    # special case: delete the head
    if head.value == value:
        delete_head()
        return

    # general case 
    prev = head
    cur = head.next

    while cur is not None:
        if cur.value == value:
            # print(f'Found it! {cur.value}')
            prev.next = cur.next
            cur.next = None
            return

        cur = cur.next
        prev = prev.next
    print("Didn't find it")



insert_at_front(45)
insert_at_front(88)
insert_at_front(12)



print_list()
# delete_head()
delete_node(12)
print_list()
