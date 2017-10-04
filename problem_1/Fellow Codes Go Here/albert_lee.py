
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



        
def oddEvenList_Helper(head, counter=0):
    #YOUR CODE GOES HERE
    
    if head.next == None:
        # This is satisfied if total length of orig. list is odd
        # ...which means the current head is the final odd mode,
        # and there are no more even nodes
        oddHead = ListNode(head.data)
        evenHead = None
        lastOddHead = oddHead
        lastOddHead.next = None

    elif head.next.next == None:
        # This is satisfied if total length of orig. list is even
        # ...which means the current head is the final odd mode
        # and there is one more final even node
        oddHead = ListNode(head.data)
        evenHead = ListNode(head.next.data)
        lastOddHead = oddHead
        lastOddHead.next = evenHead

    else:
        # Pick out topmost odd and even nodes separately from current iteration of list
        # I'm gonna think of these as the odd and even 'heads'
        # Link current 'heads' to respective odd and even 'heads' from next iteration of this function
        #   (i.e. the odd and even nodes two links down)
        # For each iteration, keep updating pointer of final odd node (picked by if cases above)
        #   and make it point to current even head 
        # Unless I'm at the orig. head, return odd and even heads and final odd node
        #   so they can be used by the previous iteration
        oddHead = ListNode(head.data)
        evenHead = ListNode(head.next.data)
        oddHead.next, evenHead.next, lastOddHead = oddEvenList_Helper(head.next.next, counter+1)
        lastOddHead.next = evenHead

    # counter lets me keep track of how far down the original list I am
    # If I'm at the original head, 
    if counter > 0:
        return oddHead, evenHead, lastOddHead
    else:
        return oddHead

    return None




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
