΢�Ź��ںţ�Сղѧpython
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = numRows
        #��ʼСղ�������б��棬Ȼ��õ����
        #�ٽ���ת��Ϊ�ַ����ģ����ﶨ��յ��б�
        res_list = []
        l = len(s)
        #���ǵ������������ʵ����Сղ����û�п���ȫ
        #����һ�У���Ӧ�ÿ��ǵ����ַ������߿��ַ���
        if n == 1:
            return s
        #����0��n-1��
        for i  in range(n):
            #���������ַ���j��ʾ����
            for j in range(l):
                #���Ǿ���Сղ���ܵ�ȡģ�ж��Ƿ��ڵ�i�����
                if j%(2*n-2) == i or j%(2*n-2) == 2*n-2-i:
                    res_list.append(s[j])
        #�����������join���б�ת��Ϊ�ַ���
        res = "".join(res_list)
        
        return res
#�ϱ߳���ʱ������


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        n = len(s)
        ans = []
        step = 2 * numRows - 2
        for i in range(numRows):
            one = i
            two = -i
            while one < n or two < n:
                if 0 <= two < n and one != two and i != numRows - 1:
                    ans.append(s[two])
                if one < n:
                    ans.append(s[one])
                one += step
                two += step
        return "".join(ans)

#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        node_length = 2*numRows - 2  # ����֮��Ĳ�
        result = ""

        if str_length == 0 or numRows == 0 or numRows == 1:
            return s

        for i in range(numRows):  # �ӵ�һ�б��������һ��
            for j in range(i, str_length, node_length):
                result += s[j]  # ��һ�к����һ��  ������ͨ�е���������
                if i != 0 and i != numRows-1 and j - 2*i + node_length < str_length:
                    result += s[j-2*i+node_length]  # �����е�����
        return result