΢�Ź��ںţ�Сղѧpython
```python
class Solution:
    def myAtoi(self, string):
        #�������������+-1������󷵻�resultʱ����sign����
        sign = 1
        result = 0
        found = False
        n = len(string)
        for char in string:
            # ����continue������ͷ�Ŀո��
            if not found and char == " ":
                continue
            # ��⵽����-��ʾ������sign��Ϊ-1
            elif not found and char == "-":
                found = True
                sign = -1
            # ��⵽����+��ʾ����
            elif not found and char == "+":
                found = True
            # ����str.isdigit()��������ַ��Ƿ�Ϊ����
            elif char.isdigit():
                found = True
                result = result * 10 + int(char)
                # ȷ���Ƿ񳬳���Χ���������ձ߽����
                if result > 2147483647 and sign == 1:
                    return 2147483647
                if result > 2147483648 and sign == -1:
                    return -2147483648
            #������������ַ�����ĸ�ȡ�����������result=0
            else:
                break
        return sign * result
```