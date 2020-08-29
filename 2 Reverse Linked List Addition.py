# LeetCode #2: Add Two Numbers in reversed linked list, return linked list of the numbers added and reversed

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        curr = ListNode()
        head = curr
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            number = v1 + v2 + carry
            if number >= 10:
                number -= 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(number)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            curr.next = ListNode(1, None)
        return head.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_nums = []
        l2_nums = []
        node = l1
        while node != None:
            l1_nums.append(str(node.val))
            node = node.next
        node = l2
        while node != None:
            l2_nums.append(str(node.val))
            node = node.next
        l1_nums.reverse()
        l2_nums.reverse()
        final = str(int("".join(l1_nums)) + int("".join(l2_nums)))
        final = final[::-1]
        print(final)
        curr = ListNode()
        head = curr
        for i, char in enumerate(final):
            curr.val = int(char)
            if i == len(final) - 1:
                curr.next = None
                break
            curr.next = ListNode()
            curr = curr.next
        return head
