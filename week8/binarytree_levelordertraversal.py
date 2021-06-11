#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        temp, queue, next_queue, ans = [], [root], [], []
        while len(queue) != 0:
            for i in queue:
                temp.append(i.val)
                if i.left is not None:
                    next_queue.append(i.left)
                if i.right is not None:
                    next_queue.append(i.right)
            ans.append(temp)
            queue = next_queue
            temp = []
            next_queue = []
        return ans 

