"""
Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was
in the input.
The first node is considered odd, the second node even and so on ...
"""

import unittest
#######################
def oddEvenList_Helper(head):
    # check if there are 2 or fewer nodes
    if (head == None) | (head.next == None):
        return head


    # initialize odd and even lists
    lastOdd = head
    lastEven = lastOdd.next
    firstEven = lastEven

    while (lastOdd.next != None) & (lastEven.next != None):
        # repoint odd to the next odd
        lastOdd.next = lastEven.next
        # update last odd
        lastOdd = lastOdd.next

        # repoint even to the next even
        lastEven.next = lastOdd.next
        # update last even
        if lastEven.next != None:
            lastEven = lastEven.next

    # point last odd to first even
    lastOdd.next = firstEven

    return head
##########################


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

#solution obtain from web
def oddEvenList(head):
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)
    while head:
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next
        head = head.next.next if even else None
    odd.next = dummy2.next
    return dummy1.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

class MyTest(unittest.TestCase):
    def test(self):
        print("runing testcases:")
        self.assertEqual(oddEvenList(head), oddEvenList_Helper(head))

# testcase
# def main():
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#     head=oddEvenList(head)
#     print ("Expected result: 1, 3, 5, 2, 4")
#     print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data))
#


if __name__ == "__main__":
    unittest.main()
