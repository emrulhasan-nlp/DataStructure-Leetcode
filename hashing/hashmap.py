"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target):
        
        mydict={}
        
        idx=[]
        for i, num1 in enumerate(nums):
            num2=target-num1
            
            if num2 in mydict:
                idx.append([mydict[num2],i])
            
            mydict[num1]=i     
        return idx

#nums = [2,7,11,15]
nums = [2,7,7,3,6,6,5,3,7,4,11,15]

target = 9
twosum=Solution()

result=twosum.twoSum(nums, target)

#######***********You cannot use the same index twice.*************
from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        
        _dict={}
        mydict=defaultdict(list)
        for i, num1 in enumerate(nums):
            num2=target-num1
            
            if num2 in _dict:
                mydict[_dict[num2]].append(i)
                
                #idx.append([mydict[num2],i])
            _dict[num1]=i 
        result=[[k, v[0]]for k, v in mydict.items()]
        
        if len(result)==1:
            return result[0]
        else:
            return result

#nums = [2,7,11,15]
nums = [2,7,7,3,6,6,5,3,7,4,11,15]

target = 9
twosum=Solution()

result=twosum.twoSum(nums, target)    
print(result)
