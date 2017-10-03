"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


# constructor for a Node of singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # type: ListNode


def oddEvenList_Helper(head):
    # YOUR CODE GOES HERE
    odd_head = head
    odd_tail = odd_head

    even_head = head.next
    even_tail = even_head

    #detach walked list from odd_tail
    odd_tail.next = None

    current = None
    #attach remaining list to current
    if even_tail is not None:
        current = even_tail.next

    #detatch walked list from even_tail
    even_tail.next = None

    # if odd_tail is not None:
    #     print("odd tail data: ", odd_tail.data)
    # else:
    #     print("odd tail is None")
    #
    # if even_tail is not None:
    #     print("even tail data", even_tail.data)
    # else:
    #     print("even tail is None")

    while current is not None:
        # print("Current data: ", current.data)
        #currently odd
        odd_tail.next = current
        odd_tail = odd_tail.next
        current = current.next
        odd_tail.next = None

        #currently even
        if current is not None:
            even_tail.next = current
            even_tail = even_tail.next
            current = current.next
            even_tail.next = None

        # if odd_tail is not None:
        #     print("odd tail data: ", odd_tail.data)
        # else:
        #     print("odd tail is None")
        #
        # if even_tail is not None:
        #     print("even tail data", even_tail.data)
        # else:
        #     print("even tail is None")
    # combine the two linked lists
    odd_tail.next = even_head
    return odd_head


# DO NOT CHANGE THIS FUNCTION
def oddEvenList(head):
    return oddEvenList_Helper(head)


# test case
def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = oddEvenList(head)
    print("Expected result: 1, 3, 5, 2, 4")
    print("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data,
                                                     head.next.next.next.data, head.next.next.next.next.data))


if __name__ == "__main__":
    main()
