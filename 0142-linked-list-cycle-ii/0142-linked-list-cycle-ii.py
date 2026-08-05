from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                ptr = head   # ✅ fixed
                while slow is not ptr:
                    slow = slow.next
                    ptr = ptr.next
                return ptr
        
        return None