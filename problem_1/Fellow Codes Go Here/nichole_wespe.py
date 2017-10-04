
"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

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
        self.link = None


def oddEvenList_Helper(head):
    # YOUR CODE GOES HERE

    first_even = head.link  # need to save B with temp pointer
    curr_node = head  # initialize while loop with head node

    i = 1
    while curr_node.link is not None:
        prev_node = curr_node  # remember for lists of even length
        next_node = curr_node.link  # place current node's link into temp holder
        curr_node.link = next_node.link  # reassign current node's link to next_node's link (i.e., skip a node)
        curr_node = next_node  # now run loop for the next node
        i += 1

    if i % 2 == 1:  # for odd-length list, connect last node to first even
        curr_node.link = first_even
    else:
        prev_node.link = first_even

    return head


# DO NOT CHANGE THIS FUNCTION
def oddEvenList(head):
    return oddEvenList_Helper(head)


#test case
def main():
    head = ListNode('A')
    head.link = ListNode('B')
    head.link.link = ListNode('C')
    head.link.link.link = ListNode('D')
    head.link.link.link.link = ListNode('E')
    head = oddEvenList(head)
    print ("Expected result: A, C, E, B, D")
    print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.link.data, head.link.link.data,
                                                      head.link.link.link.data, head.link.link.link.link.data))

    # to traverse the list and print it out
    # tmp = head
    # while tmp is not None:
    #     print tmp.data
    #     tmp = tmp.link


if __name__ == "__main__":
    main()