#��עСղѧpython
#��עСղѧpython
#��עСղѧpython
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        diff = float("inf")
        for i in xrange(0, len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum > target:
                    if abs(target - sum) < diff:
                        diff = abs(target - sum)
                        ans = sum
                    end -= 1
                else:
                    if abs(target - sum) < diff:
                        diff = abs(target - sum)
                        ans = sum
                    start += 1
        return ans


#beat100%
```
class Solution:
    def threeSumClosest(self, nums, target):
        # ���ź��򣬱��ڱȽ�
        nums.sort()
        length = len(nums)
        closest = []
        #�����ǲ��ù̶���һ����С�����Ӻ�����Ƭ���������м�ƽ�
        for i, num in enumerate(nums[0:-2]):
            l,r = i+1, length-1	 # i֮�����Ƭ���ӵ�һ�������һ�����бƽ�				
            if num+nums[r]+nums[r-1] < target:  
            #�̶�������������������С��Ŀ��ֵ����ʱ�����ڹ̶�һ��������ӽ������
                closest.append(num+nums[r]+nums[r-1])
            elif num+nums[l]+nums[l+1] > target:
            #�̶�����������С������������Ŀ��ֵ����ʱ�����ڹ̶�һ��������ӽ������
                closest.append(num+nums[l]+nums[l+1])
            else: 
                while l < r: # ��l<r,���ڶ�����С�ڵ�������ʱ������ִ��
                    closest.append(num+nums[l]+nums[r])
                    if num+nums[l]+nums[r] < target:
                        l += 1 # ���С��Ŀ��ֵ���ڶ���������һ��
                    elif num+nums[l]+nums[r] > target:
                        r -= 1 # �������Ŀ��ֵ����������ǰ��һ��
                    else:
                        return target # ǡ�õ��ڣ�ֻ��һ���⣬��ֱ�ӷ���
        #�ϱ߽����ܵ����append��closest�������Ȱ���ľ���ֵ����󷵻ص�һ��            
        closest.sort(key=lambda x:abs(x-target))
        return closest[0]
```