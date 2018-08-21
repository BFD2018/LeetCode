#��ӭ��עСղѧpython
```
class Solution(object):
    def generateParenthesis(self, n):
        #�Ӻ��� �������������� ���ݹ�˼·Ŷ
        def generate(A = []):
            if len(A) == 2*n: #������ɵ��������г���Ϊ2n�����ж��Ƿ���Ч
                if valid(A):
                    ans.append("".join(A)) #��Ч����������ӽ�ans
            else: 
            #����������ͨ���ݹ����generate���ɣ��������Ч����һ�������ַ�pop����������generate
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        #�ж����ɵĳ���Ϊ2n���������Ƿ���Ч
        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        #������б�ans�洢��ͨ������generateִ��ֱ�����н�����ж���һ�����
        ans = []
        generate()
        return ans
```

```
class Solution(object):
    def generateParenthesis(self, N):
        #�����ǵݹ� ��ֻ�������Ǳ����г����е������ַ���
        #���ǵ���ǰ�����ַ���������Ȼ������Чʱ�����
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            #����ȽϹؼ�����Ҫ�ú�����£��������еĽ��⡣
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        ans = []
        backtrack()
        return ans
```