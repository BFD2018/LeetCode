```
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #����һ�����б�����ԭ�б�����
        result = []
        nums.sort()
        #ԭ�б���
        ly_len = len(nums)
        #��������
        for i in range(ly_len-1):
            for j in range(i + 1,ly_len):
                #��ǰ����֮�͵��෴�����б���Ƭnums[j+1:]�м���
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    ly = [nums[i],nums[j],-(nums[i]+nums[j])]
                    if ly not in result:
                        result.append(ly)   
        return result
```��ʱ������

```beat90
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #ͬ�ϣ����б������
        res = []
        nums.sort()
        #�̶�һ������������������ƥ�䣬��0
        for i in range(0, len(nums)):
            #�������ܴ�����ȵ�������������[-1,-1,0����];continue�´�ѭ��
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i] #����������֮��Ϊtarget
            start, end = i + 1, len(nums) - 1#�Ӻ����б���Ƭ�������м�ƽ�
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1  #�����λ֮�ʹ���Ŀ��ֵ��β��������һ
                elif nums[start] + nums[end] < target:
                    start += 1#�����λ֮��С��Ŀ��ֵ���ײ�������һ
                else:#����Ŀ��ֵ�����¼��ǰһ��⣬��Ѱ��������
                    res.append((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1 #���β���������������ʱ��β��������һ
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1#����ײ��������������ʱ���ײ�������һ
        return res
```