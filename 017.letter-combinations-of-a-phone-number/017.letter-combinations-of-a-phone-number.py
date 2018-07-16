#��עСղѧpython
#��עСղѧpython
#��עСղѧpython
beat 97
```
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return [] # �����ַ�Ϊ��ʱ
        #����һ���ֵ䣬��ֵ����ʽ��ŵ绰�����������ַ���Ӧ��ϵ
        table = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        
        result = [''] # �������б����ڴ�Ž��
        for digit in digits: # ������digits�����ζ�ÿ�������ַ�����
            str_list = [] # �趨һ���м���̴���б�
            for char in table[digit]: # resultΪ��Ŵ������ǰ�������ַ�
                #���ｫ�����ֶ�Ӧ���ַ�ƴ�ӵ�ǰ�����е�result��
                str_list += [x + char for x in result] 
            result = str_list #������õ�ǰ�����ֽ�������result�������������λ
        return result
```

#���ϴ��룬ͬ��˼·������࣡
```
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2': [i for i in "abc"], '3': [i for i in "def"], \
                '4': [i for i in "ghi"], '5': [i for i in "jkl"], \
                '6': [i for i in "mno"], '7': [i for i in "pqrs"],\
                '8': [i for i in "tuv"], '9': [i for i in "wxyz"]}
								
        def helper(digits, comb = ""):
            if len(digits) > 0:
                for i in dict[digits[0]]:
                    yield from helper(digits[1:], comb + i)
            else:
                yield comb
        return list(helper(digits)) if digits != "" else []
```