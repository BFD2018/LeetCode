΢�Ź��ںţ�Сղѧpython
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x /= 10
        return sign * ans if ans <= 0x7fffffff else 0


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #�ȼ�¼����
        sign = [1,-1][x < 0]
        #����������ת����Ų��䣬�����þ���ֵ�������з�ת�����ԭ�з��ż���
        rst = sign * int(str(abs(x))[::-1])
        #���ط�תֵ������32λΪ0
        return rst if -(2**31)-1 < rst < 2**31 else 0


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #����һ�����ַ�����˼·�ǽ������ַ���ͨ�����¼��㷴ת��
        #ת�����ַ�����תת��������
        s = ''
        while x//10 != 0:
            num = x % 10
            s = s + str(num)
            x //= 10
        s = s + str(x) #������λ���߱�����Ǹ�λ�����������  

        return int(s)