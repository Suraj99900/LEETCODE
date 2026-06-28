# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reveres_node(self, headListNode: ListNode) -> ListNode:
        pre = None
        curr = headListNode
        
        while curr:
            nxt = curr.next    
            curr.next = pre    
            pre = curr         
            curr = nxt        
            
        return pre    
    def returnNumber(self,node:ListNode):
        curr = node 
        aData= ""
        while curr is not None:
            aData = aData + str(curr.val)
            curr = curr.next
        return aData
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reveres_node(l1)
        l2 = self.reveres_node(l2)
     
        l1= self.returnNumber(l1)
        l2 =self.returnNumber(l2)
        
        l3 = str(int(l1)+int(l2))

        currentNode = None
        aDataNew = []
        currentNode = None
        for iEle in l3:
            currentNode = ListNode(int(iEle), currentNode)
        return currentNode
       
