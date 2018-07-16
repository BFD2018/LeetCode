
```
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #������ַ������
        ans = ""
        #����һ���ֵ��һ���б����ֵ�ƥ���Ӧ���б����������ӵ����ַ��������
        values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        literals = ["M", "D", "C", "L", "X", "V", "I"]
        #���γ���1000��100��10��1�����д���
        for idx in [0, 2, 4]:
            #k��ʾ�����õ����̣�����ʵ����ֻ���ڳ���1000ʱ���õ��ϣ����Դ��������ԣ�
            k = num // values[literals[idx]]
            #re��ʾȡģ���ٳ��Ե�һ���������õ�����
            re = (num % values[literals[idx]]) // values[literals[idx + 2]]
            #Сղ���ѣ�������1-3999��Χ�ڣ����Գ���1000�����Ϊ3
            ans += k * literals[idx]
            #������Բ�ͬ������������ദ��
            #ȡģΪ9ʱ
            if re >= 9:
                ans += literals[idx + 2] + literals[idx] 
            #ȡģΪ5��6��7��8ʱ
            elif re >= 5:
                ans += literals[idx + 1] + (re - 5) * literals[idx + 2]
            #ȡģΪ4ʱ
            elif re == 4:
                ans += literals[idx + 2] + literals[idx + 1]
            #ȡģΪ0��1��2��3ʱ
            else:
                ans += re * literals[idx + 2]
            #ȡģ�������һ��ѭ��
            num %= values[literals[idx + 2]]
        return ans
        
```