from typing import List, Optional


class listNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next



class Test_Solution():

    def mergen(self,l1: Optional[listNode],l2: Optional[listNode]):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<=l2.val:
            l1.next=self.mergen(l1.next,l2)
            return l1
        else:
            l2.next=self.mergen(l2.next,l1)
            return l2






if __name__ == '__main__':
    xx=Test_Solution()
    xx.mergen([1,2,4],[1,3,5])


