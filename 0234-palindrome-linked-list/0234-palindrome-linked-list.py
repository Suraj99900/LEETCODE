# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def traverseNormal(self, node: ListNode):
        current  = node
        returnNormalNode = ''
        ReverseNode = ''
        while current != None:
            returnNormalNode = returnNormalNode + str(current.val)
            current  = current.next

        current  = node
        while current != None:
            ReverseNode = str(current.val) + ReverseNode
            current  = current.next
        # print(ReverseNode)
        return ( True if returnNormalNode == ReverseNode else False ) 
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.traverseNormal(head)