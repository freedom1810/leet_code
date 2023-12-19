# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_res  = ListNode()
        l_temp = l_res
        temp = 0
        while l1 is not None or l2 is not None:
            
            if l1 is not None:
                temp += l1.val
                l1 = l1.next
                
            if l2 is not None:
                temp += l2.val
                l2 = l2.next
                

            l_temp.val = temp%10
            temp = temp//10
            
            if l1 is None and l2 is None: 
                break
            
            l_temp.next = ListNode()
            l_temp = l_temp.next
        
        if temp != 0:
            l_temp.next = ListNode()
            l_temp = l_temp.next
            l_temp.val = temp
                
        return l_res