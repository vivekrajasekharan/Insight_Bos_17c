
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

# 1 2 3 4 5

# def oddEvenList_Helper(head):
    #YOUR CODE GOES HERE
    # # start with head, find 3 and set head.next=
    # new=head  #odd first
    # even=head.next # even first
    # count=1
    # while new.next:
    #     count+=1
    #     curr=new.next
    #     print curr.data
    #     if count%2 > 0: # Odd
    #         new.next=curr
    #         new=curr
    #         print new.data
    #     # else:
    #     #     new.nextNode = None
    #     #     temp.nextNode = head2
    #     #     break
    # head=new
    #
    # # while currnext != None:
    # #     count += 1
    # #     if count % 2 ==0:  # Even
    # #         curr.next = currnext
    # # head=head.next
    # return head

def oddEvenList_Helper(head):
    node=head
    nodeeven=head.next
    node2=head.next

    while node.next:
        # Link odd nodes
        node.next=nodeeven.next
        node=nodeeven.next

        # Link even nodes
        nodeeven.next=node.next
        nodeeven=node.next

        # Link last odd node to first even node
        if node.next == None:
            node.next=node2
            break;

    return head





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