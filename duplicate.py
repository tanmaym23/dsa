# remove duplicate from a linklist

class solution:
    def delDuplicates(self,head):
        cur=head
        while cur:
            while cur.next and cur.next.value==cur.value:
                cur.next=cur.next.next
            cur=cur.next
        return head
    