```python
#��û�з���Сղ���컻�˸���̱�������������
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        #������������ƥ��ʵ�֣�������re��
        #��ʼ�ǵ�һ���ַ���Ϊƥ��ģʽ
        prefix = strs[0]
        for i in range(1, len(strs)):
            match = re.match(prefix, strs[i])
            while not match:
                #û��ƥ�䵽����ģʽ�������ȥ��һ���ַ�
                prefix = prefix[:-1]
                match = re.match(prefix, strs[i])
        return prefix
```

```python
#��û�з���Сղ���컻�˸���̱�������������
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #���Ǽ������������������0��1���ַ���ʱ
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        l_strs = len(strs)
        #��ȡ�ַ������г�����̵ĳ���ֵ��ע�͵�����һ����ȡ��ʽ��
        #����ʹ�õ�����һ��min��ʽ
        # for l in range(1,l_strs):
        #     if len(strs[l]) < j_max:
        #         j_max = len(strs[l])
        j_max = min([len(str) for str in strs])
        
        #�����ǽ�����ַ������ַ����������������ַ����Ա�
        #����������ַ����ĵ�һ���ַ����ڶ����������жԱ�
        for j in range(0,j_max):
            for i in range(1, l_strs):
                #�������ַ���ͬ��ʱ��˵������������ͬ�ַ���
                if strs[0][j] != strs[i][j]:
                    return strs[0][:j]
        #�����������ַ���
        return strs[0][:j_max]
```