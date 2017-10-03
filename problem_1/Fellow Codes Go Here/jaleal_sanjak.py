
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

#constructor for a Node of singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def oddEvenList_Helper(head):
    #YOUR CODE GOES HERE

    odd = head
    even = head.next
    evenFirst = even
    while True: 
        # go through the list
        # if either points to None
        if (odd.next is None or even.next is None):
            odd.next = evenFirst # connect the end of odd to beginning of even
            break # and we are done
        # otherwise, there are more nodes
        # start with the odd nodes
        odd.next = even.next # make odd point to what even points to, which is the next odd node
        odd = even.next # then move odd to what even points to, which is the next odd node
        #if odd now points to None
        if odd.next is None:
            # We are at the end of the list
            even.next = None # set the end of even to None to regain proper linked list form
            odd.next = evenFirst # connect the end of odd to beginning of even
            break # and we are done
        
        # otherwise, there are more even nodes also
        even.next = odd.next # make even point to what odd points to, which is the next odd node
        even = odd.next # then move even to what odd points to, which is 
    return(head)


#DO NOT CHANGE THIS FUNCTION
def oddEvenList(head):
    return oddEvenList_Helper(head)


#test case
def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head =  oddEvenList(head)
    print ("Expected result: 1, 3, 5, 2, 4")
    print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data))

if __name__ == "__main__":
    main()