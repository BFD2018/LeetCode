```
class Solution(object):
    def romanToInt(self, s):
        #����һ���ֵ䣬���������ֵ���������оٳ�����
        map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        #��ʼΪ0
        i,res=0,0
        while i<len(s):
            #��ͷ��β���в��ң�s[i:i+2]��ʾ��Ƭ��ע������ҿ���
            if i<len(s)-1 and map.get(s[i:i+2]) != None:
                i,res =i+2,res+map[s[i:i+2]]
            #��ͬʱƥ���������������ַ������ֵ�key����ƥ��ʱ����������һ���ַ�ƥ��
            else:
                if map.get(s[i])!=None:
                    i,res=i+1,res+map[s[i]]
        return res
```

```
class Solution(object):
    def romanToInt(self, s):
        #���ﹹ���ֵ䵥�ַ���������
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        #��¼ǰһ���ַ���������֣���ʼΪ0
        prev_value = running_total = 0
        #�ӵ�λ����λ�����δ���
        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            #�����ǰֵС��ǰһλ���ұߣ�����ʾ�����������Ϊ��-��
            if int_val < prev_value:
                running_total -= int_val
            #�����ǰֵ��С��ǰһλ���ұߣ���Ϊ�����ӵ����
            else:
                running_total += int_val
            #��¼��ǰֵΪ��ʷֵ����������һ��ѭ��
            prev_value = int_val
        return running_total
```