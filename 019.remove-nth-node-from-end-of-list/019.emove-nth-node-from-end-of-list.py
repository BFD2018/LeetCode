#��עСղѧpython
 ```
class Solution:
    #��Ӧ�ϱ�Сղ˵�ĵڶ���˼·
    def removeNthFromEnd(self, head, n):
        first = second = head
        #����һ����ָ�롯�ƶ� n ��λ��
        for _ in range(n):
            first = first.next
        #�������������firstָ�������һ���ڵ㣬��Ҫɾ���ǵ�һ���ڵ㣨������n����
        if not first:
            return head.next
        #��������ָ�롯ͬ������
        #ֱ��firstָ�������һ���ڵ㣨������ָ�롯ʼ�ձ�����ͬ�����
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
```