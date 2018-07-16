```
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #��ʼ��Ϊ������Ϊ0����������������ޣ�
        max_area = 0
        n = len(height)
        #�����е�û�����������������������Сղ��֮ǰ�ܶ��ⶼд����ϸע�ͣ�����׸��
        for i in range(n):
            for j in range(i,n):
                area = (j - i)*min(height[i],height[j])
                if area >= max_area:
                    max_area = area
        return max_area
```

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #�����ʼ���Ϊ0����������ģ��ָ��ָ����ͷ
        max_area = left = 0
        right = len(height) - 1
        #ѭ��ִ������
        while left < right:
            #������
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            #����е�ͷ������
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
```