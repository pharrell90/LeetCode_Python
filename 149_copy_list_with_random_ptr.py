'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

runtime
'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:

    def copy_random_list(self, head):
        if not head: return None

        temp = head
        while temp:
            new_node = RandomListNode(temp.label)
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next.next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        new_head = head.next
        p_old = head
        p_new = new_head
        while p_new.next:
            p_old.next = p_new.next
            p_old = p_old.next
            p_new.next = p_old.next
            p_new = p_new.next

        p_old.next = None
        p_new.next = None

        return new_head

