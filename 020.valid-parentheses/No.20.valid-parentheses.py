#��ӭ��ע΢�Ź��ں� Сղѧpython
˼·һ��
```
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        # ���ַ��� ���������ţ�����Ҳ����Ч��
        if n == 0:
            return True
        # �ַ�������Ϊ���� ��������ƥ��
        if n % 2 != 0:
            return False
        #�������˸�һ���� ������python��replace�޳��ɶԵ�����    
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        return s == ''
```
˼·��

```
class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            #������������append���б�
            if char in ["(","{","["]:
                stack.append(char)
            elif not stack: #�������ų�ֻ�������ŵ�������磺������
                return False
            #�����ǵ�������ʱ����pop���ɶԵ�����
            elif (char == ")") and (stack[len(stack)-1]=="("):
                stack.pop()
            elif (char == "}") and (stack[len(stack)-1]=="{"):
                stack.pop()
            elif (char == "]") and (stack[len(stack)-1]=="["):
                stack.pop()
            else:
                return False
        return len(stack)==0 #��Ч������ʱ�����������pop�������ַ���������Ϊ0
```
